"""
📊 ANALYTICS PORTAL: Pandas Engine
--------------------------------------------------
- Descriptive Stats: Tính toán Mean, Median, Std Dev thông qua Vectorization.
- Neural Mapping: Tạo biểu đồ phân phối điểm (Histogram, Grade Analysis).
- Thread-Safe Viz: Cơ chế khóa luồng (Chart Lock) đảm bảo tính ổn định của Server.
"""
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Any
import matplotlib
# Force non-interactive backend for web stability
matplotlib.use('Agg')
from matplotlib.figure import Figure
import seaborn as sns
from pathlib import Path
import logging
import threading

logger = logging.getLogger(__name__)

# Global lock for chart generation to prevent threading crashes
chart_lock = threading.Lock()

class ExamDataAnalyzer:
    """Analyze exam data using Pandas DataFrames"""
    
    def __init__(self, data_source: str = None):
        """
        Initialize analyzer with data source
        
        Args:
            data_source: Path to CSV/JSON file or DataFrame
        """
        self.df = None
        self.original_df = None
        
        if data_source:
            self.load_data(data_source)
    
    def load_data(self, source: str) -> pd.DataFrame:
        """
        Load data from file or create from list of dicts
        
        Args:
            source: File path (CSV/JSON) or list of records
            
        Returns:
            Loaded DataFrame
        """
        try:
            if isinstance(source, str):
                if source.endswith('.csv'):
                    self.df = pd.read_csv(source)
                elif source.endswith('.json'):
                    self.df = pd.read_json(source)
                else:
                    raise ValueError("Unsupported file format")
            elif isinstance(source, list):
                self.df = pd.DataFrame(source)
            else:
                self.df = source
            
            self.original_df = self.df.copy()
            
            # Display info
            logger.info(f"✓ Loaded {len(self.df)} records")
            print(f"\nDataFrame Shape: {self.df.shape[0]} rows × {self.df.shape[1]} columns")
            
            return self.df
            
        except Exception as e:
            logger.error(f"✗ Failed to load data: {e}")
            return None
    
    def display_dataframe_info(self):
        """Display comprehensive DataFrame information"""
        print("\n" + "=" * 60)
        print("STEP 7.1: DataFrame Ingestion & Inspection")
        print("=" * 60)
        print("\nDataFrame Info:")
        print(f"Shape: {self.df.shape}")
        print(f"Total Records: {len(self.df)}")
        print(f"Total Columns: {len(self.df.columns)}")
        print(f"\nColumns and Data Types:")
        print(self.df.info())
        
        print("\n✓ Data Types:")
        for col, dtype in self.df.dtypes.items():
            print(f"  {col}: {dtype}")
    
    def ensure_numeric_columns(self, score_column: str = 'processed_score') -> pd.DataFrame:
        """
        Convert score columns to numeric type
        
        Args:
            score_column: Name of score column to convert
            
        Returns:
            DataFrame with numeric columns
        """
        if score_column in self.df.columns:
            self.df[score_column] = pd.to_numeric(
                self.df[score_column], 
                errors='coerce'
            )
            print(f"✓ Converted '{score_column}' to numeric type")
        
        return self.df
    
    def create_feature_columns(self) -> pd.DataFrame:
        """
        Create calculated feature columns from raw data
        """
        print("\n" + "=" * 60)
        print("STEP 7.2: Feature Engineering (Calculated Columns)")
        print("=" * 60)
        
        # Determine score column (support both processed_score and final_grade)
        score_col = 'processed_score'
        if score_col not in self.df.columns and 'final_grade' in self.df.columns:
            score_col = 'final_grade'

        if score_col in self.df.columns:
            self.df['processed_score'] = pd.to_numeric(self.df[score_col], errors='coerce')
        else:
            logger.error("❌ Critical: No score column found in data.")
            return self.df
        
        # Create score grade classification
        def get_grade(score):
            if pd.isna(score):
                return 'Unknown'
            if score >= 8.5:
                return 'A'
            elif score >= 7.0:
                return 'B'
            elif score >= 5.5:
                return 'C'
            else:
                return 'D'
        
        self.df['grade'] = self.df['processed_score'].apply(get_grade)
        print("✓ Created 'grade' column (A/B/C/D classification)")
        
        # Create performance category
        def get_performance(score):
            if pd.isna(score):
                return 'Unknown'
            if score >= 8.0:
                return 'Excellent'
            elif score >= 7.0:
                return 'Good'
            elif score >= 6.0:
                return 'Satisfactory'
            else:
                return 'Needs Improvement'
        
        self.df['performance'] = self.df['processed_score'].apply(get_performance)
        print("✓ Created 'performance' column")
        
        # Extract year if not already done
        if 'semester_info_year' not in self.df.columns and 'semester_info' in self.df.columns:
            self.df['year'] = self.df['semester_info'].apply(
                lambda x: x.get('year') if isinstance(x, dict) else None
            )
            print("✓ Extracted 'year' from semester info")
        
        # Extract semester if not already done
        if 'semester_info_semester' not in self.df.columns and 'semester_info' in self.df.columns:
            self.df['semester'] = self.df['semester_info'].apply(
                lambda x: x.get('semester') if isinstance(x, dict) else None
            )
            print("✓ Extracted 'semester' from semester info")
        
        print(f"\n✓ Total new features created: 4")
        print("\nNew Columns:")
        print(self.df[['processed_score', 'grade', 'performance']].head())
        
        return self.df
    
    def get_descriptive_statistics(self) -> pd.DataFrame:
        """
        Generate descriptive statistics for numerical columns
        
        Returns:
            DataFrame with statistics
        """
        print("\n" + "=" * 60)
        print("STEP 7.3: Market Descriptive Statistics")
        print("=" * 60)
        
        # Get numeric columns
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        stats = self.df[numeric_cols].describe()
        print("\n✓ Statistical Summary:")
        print(stats)
        
        # Additional statistics
        print("\n✓ Additional Statistics:")
        print(f"  Mean Score: {self.df['processed_score'].mean():.2f}")
        print(f"  Median Score: {self.df['processed_score'].median():.2f}")
        print(f"  Std Dev: {self.df['processed_score'].std():.2f}")
        print(f"  Min Score: {self.df['processed_score'].min():.2f}")
        print(f"  Max Score: {self.df['processed_score'].max():.2f}")
        
        # Find highest scoring record
        if 'processed_score' in self.df.columns:
            max_idx = self.df['processed_score'].idxmax()
            max_record = self.df.loc[max_idx]
            print(f"\n✓ Highest Score Record:")
            print(f"  Score: {max_record['processed_score']}")
            print(f"  Course: {max_record.get('course_name', 'Unknown')}")
            print(f"  Class: {max_record.get('class_name', 'Unknown')}")
        
        return stats
    
    def segment_by_performance(self) -> Dict[str, pd.DataFrame]:
        """
        Create segments based on performance levels
        
        Returns:
            Dictionary of segmented DataFrames
        """
        print("\n" + "=" * 60)
        print("STEP 7.4: Grouping and Segmentation Analysis")
        print("=" * 60)
        
        segments = {}
        
        # Segment by grade
        if 'grade' in self.df.columns:
            print("\n✓ Segmentation by Grade:")
            grade_segments = self.df.groupby('grade').size()
            print(grade_segments)
            segments['by_grade'] = self.df.groupby('grade')
            
            for grade, group in self.df.groupby('grade'):
                print(f"  {grade}: {len(group)} records")
        
        # Segment by performance
        if 'performance' in self.df.columns:
            print("\n✓ Segmentation by Performance:")
            perf_segments = self.df.groupby('performance').size()
            print(perf_segments)
            segments['by_performance'] = self.df.groupby('performance')
        
        # Segment by class
        if 'class_name' in self.df.columns:
            print("\n✓ Segmentation by Class:")
            class_segments = self.df.groupby('class_name').size()
            print(class_segments)
            segments['by_class'] = self.df.groupby('class_name')
        
        # High performers
        excellent = self.df[self.df['processed_score'] >= 8.5]
        print(f"\n✓ Premium/Excellent Performers (Score >= 8.5): {len(excellent)}")
        print("\nFirst 5 Premium Records:")
        print(excellent[['course_name', 'class_name', 'processed_score', 'grade']].head())
        
        segments['premium'] = excellent
        
        return segments
    
    def create_visualizations(self, output_dir: str = "visualizations"):
        """
        Create market trend visualizations using thread-safe OO API
        """
        print("\n" + "=" * 60)
        print("STEP 7.5: Visualizing Market Trends (Thread-Safe)")
        print("=" * 60)
        
        Path(output_dir).mkdir(exist_ok=True)

        # Use a lock to ensure only one thread generates charts at a time
        with chart_lock:
            try:
                # Plot 1: Score Distribution (Histogram)
                print("\n✓ Creating Visualization 1: Score Distribution")
                fig1 = Figure(figsize=(10, 6))
                ax1 = fig1.add_subplot(111)
                fig1.set_facecolor('#1e293b')
                ax1.set_facecolor('#1e293b')

                # Check if we have data
                if not self.df.empty and 'processed_score' in self.df.columns:
                    sns.histplot(self.df['processed_score'].dropna(), bins=15, kde=True, color='#38bdf8', ax=ax1)

                ax1.set_title('Distribution of Exam Scores', fontsize=16, fontweight='bold', color='#f1f5f9', pad=20)
                ax1.set_xlabel('Score (0-10)', fontsize=12, color='#94a3b8')
                ax1.set_ylabel('Count', fontsize=12, color='#94a3b8')
                ax1.tick_params(colors='#94a3b8')
                ax1.grid(alpha=0.1)

                fig1.tight_layout()
                plot1_path = Path(output_dir) / "score_distribution.png"
                fig1.savefig(plot1_path, dpi=120, bbox_inches='tight', facecolor='#1e293b')
                logger.info(f"✓ Saved: {plot1_path}")

                # Plot 2: Grade Distribution (Bar Chart)
                print("✓ Creating Visualization 2: Grade Analysis")
                fig2 = Figure(figsize=(10, 6))
                ax2 = fig2.add_subplot(111)
                fig2.set_facecolor('#1e293b')
                ax2.set_facecolor('#1e293b')

                if 'grade' in self.df.columns and not self.df.empty:
                    grade_counts = self.df['grade'].value_counts().sort_index()
                    if not grade_counts.empty:
                        colors = ['#22c55e', '#38bdf8', '#f59e0b', '#ef4444', '#94a3b8']
                        grade_counts.plot(kind='bar', color=colors[:len(grade_counts)], ax=ax2)

                ax2.set_title('Total Counts per Grade Level', fontsize=16, fontweight='bold', color='#f1f5f9', pad=20)
                ax2.set_xlabel('Grade', fontsize=12, color='#94a3b8')
                ax2.set_ylabel('Number of Subjects', fontsize=12, color='#94a3b8')
                ax2.tick_params(colors='#94a3b8')
                ax2.grid(alpha=0.1, axis='y')

                fig2.tight_layout()
                plot2_path = Path(output_dir) / "grade_performance.png"
                fig2.savefig(plot2_path, dpi=120, bbox_inches='tight', facecolor='#1e293b')
                logger.info(f"✓ Saved: {plot2_path}")

                print(f"\n✓ Visualizations saved to: {Path(output_dir).resolve()}")
                return [str(plot1_path), str(plot2_path)]
            except Exception as e:
                logger.error(f"Chart generation failed: {e}")
                import traceback
                logger.error(traceback.format_exc())
                return []

# Example usage
if __name__ == "__main__":
    from data_persistence import DataPersistence
    
    print("=" * 60)
    print("OBJECTIVE 2: DATAFRAME ANALYSIS & VISUALIZATION")
    print("=" * 60)
    
    # Create sample data
    sample_data = [
        {'id': 'E001', 'course_name': 'Giáo Dục Thể Chất', 'class_name': 'K65-A', 'processed_score': 8.5, 'semester_info': {'year': 2022, 'semester': 1}},
        {'id': 'E002', 'course_name': 'Triết Học', 'class_name': 'K65-B', 'processed_score': 7.2, 'semester_info': {'year': 2022, 'semester': 1}},
        {'id': 'E003', 'course_name': 'Tiếng Anh', 'class_name': 'K66-01', 'processed_score': 9.0, 'semester_info': {'year': 2022, 'semester': 1}},
        {'id': 'E004', 'course_name': 'Lập Trình Python', 'class_name': 'K65-A', 'processed_score': 6.5, 'semester_info': {'year': 2022, 'semester': 1}},
        {'id': 'E005', 'course_name': 'Toán Cao Cấp', 'class_name': 'K66-02', 'processed_score': 7.8, 'semester_info': {'year': 2022, 'semester': 1}},
    ]
    
    # Analyze
    analyzer = ExamDataAnalyzer(sample_data)
    
    # Step 1: Display info
    analyzer.display_dataframe_info()
    
    # Step 2: Create features
    analyzer.create_feature_columns()
    
    # Step 3: Statistics
    analyzer.get_descriptive_statistics()
    
    # Step 4: Segmentation
    segments = analyzer.segment_by_performance()
    
    # Step 5: Visualizations
    analyzer.create_visualizations()
    
    print("\n✓ Analysis Complete!")
