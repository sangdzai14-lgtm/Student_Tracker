"""
Data Persistence Module
Saves cleaned data to JSON and CSV formats
"""
import json
import csv
from typing import List, Dict, Any
from pathlib import Path
import logging
from datetime import datetime
import os

logger = logging.getLogger(__name__)

class DataPersistence:
    """Handles saving scraped and cleaned data to disk"""
    
    def __init__(self, data_dir: str = "scraped_data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        
        self.json_file = self.data_dir / "scraped_data.json"
        self.csv_file = self.data_dir / "scraped_data.csv"
        self.backup_dir = self.data_dir / "backups"
        self.backup_dir.mkdir(exist_ok=True)
    
    def save_to_json(self, records: List[Dict], create_backup: bool = True) -> str:
        """
        Save records to JSON file
        
        Args:
            records: List of exam records to save
            create_backup: Whether to create timestamped backup
            
        Returns:
            Path to saved JSON file
        """
        try:
            # Create backup if file exists
            if self.json_file.exists() and create_backup:
                self._create_backup(self.json_file)
            
            # Save data
            with open(self.json_file, 'w', encoding='utf-8') as f:
                json.dump({
                    'metadata': {
                        'total_records': len(records),
                        'timestamp': datetime.now().isoformat(),
                        'source': 'Bac Duy University Intelligence'
                    },
                    'data': records
                }, f, ensure_ascii=False, indent=2)
            
            logger.info(f"✓ Saved {len(records)} records to {self.json_file}")
            return str(self.json_file)
            
        except Exception as e:
            logger.error(f"✗ Failed to save JSON: {e}")
            raise
    
    def save_to_csv(self, records: List[Dict], create_backup: bool = True) -> str:
        """
        Save records to CSV file
        
        Args:
            records: List of exam records to save
            create_backup: Whether to create timestamped backup
            
        Returns:
            Path to saved CSV file
        """
        try:
            if not records:
                logger.warning("No records to save to CSV")
                return str(self.csv_file)
            
            # Create backup if file exists
            if self.csv_file.exists() and create_backup:
                self._create_backup(self.csv_file)
            
            # Extract all possible fieldnames
            fieldnames = self._get_csv_fieldnames(records)
            
            # Save data
            with open(self.csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                
                for record in records:
                    # Handle nested dicts by flattening them
                    flattened = self._flatten_record(record)
                    writer.writerow(flattened)
            
            logger.info(f"✓ Saved {len(records)} records to {self.csv_file}")
            return str(self.csv_file)
            
        except Exception as e:
            logger.error(f"✗ Failed to save CSV: {e}")
            raise
    
    def save_both(self, records: List[Dict]) -> Dict[str, str]:
        """Save records to both JSON and CSV"""
        json_path = self.save_to_json(records)
        csv_path = self.save_to_csv(records)
        
        return {
            'json': json_path,
            'csv': csv_path,
            'total_records': len(records)
        }
    
    def load_from_json(self) -> List[Dict]:
        """Load records from JSON file"""
        try:
            if not self.json_file.exists():
                logger.warning(f"JSON file not found: {self.json_file}")
                return []
            
            with open(self.json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                records = data.get('data', [])
                logger.info(f"✓ Loaded {len(records)} records from JSON")
                return records
                
        except Exception as e:
            logger.error(f"✗ Failed to load JSON: {e}")
            return []
    
    def load_from_csv(self) -> List[Dict]:
        """Load records from CSV file"""
        try:
            if not self.csv_file.exists():
                logger.warning(f"CSV file not found: {self.csv_file}")
                return []
            
            records = []
            with open(self.csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    records.append(dict(row))
            
            logger.info(f"✓ Loaded {len(records)} records from CSV")
            return records
            
        except Exception as e:
            logger.error(f"✗ Failed to load CSV: {e}")
            return []
    
    def _create_backup(self, file_path: Path):
        """Create timestamped backup of existing file"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"{file_path.stem}_{timestamp}{file_path.suffix}"
            backup_path = self.backup_dir / backup_name
            
            with open(file_path, 'r', encoding='utf-8') as src:
                with open(backup_path, 'w', encoding='utf-8') as dst:
                    dst.write(src.read())
            
            logger.info(f"✓ Created backup: {backup_path}")
        except Exception as e:
            logger.warning(f"Failed to create backup: {e}")
    
    def _flatten_record(self, record: Dict) -> Dict:
        """Flatten nested dictionaries for CSV"""
        flattened = {}
        for key, value in record.items():
            if isinstance(value, dict):
                for nested_key, nested_value in value.items():
                    flattened[f"{key}_{nested_key}"] = nested_value
            else:
                flattened[key] = value
        return flattened
    
    def _get_csv_fieldnames(self, records: List[Dict]) -> List[str]:
        """Extract all unique field names from records"""
        fieldnames = set()
        for record in records:
            for key in record.keys():
                if isinstance(record[key], dict):
                    for nested_key in record[key].keys():
                        fieldnames.add(f"{key}_{nested_key}")
                else:
                    fieldnames.add(key)
        return sorted(list(fieldnames))
    
    def get_file_info(self) -> Dict[str, Any]:
        """Get information about saved data files"""
        info = {
            'json_exists': self.json_file.exists(),
            'csv_exists': self.csv_file.exists(),
            'json_path': str(self.json_file),
            'csv_path': str(self.csv_file)
        }
        
        if self.json_file.exists():
            info['json_size'] = self.json_file.stat().st_size
            info['json_modified'] = datetime.fromtimestamp(
                self.json_file.stat().st_mtime
            ).isoformat()
        
        if self.csv_file.exists():
            info['csv_size'] = self.csv_file.stat().st_size
            info['csv_modified'] = datetime.fromtimestamp(
                self.csv_file.stat().st_mtime
            ).isoformat()
        
        return info

# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("STEP 5: DATA PERSISTENCE (JSON/CSV OUTPUT)")
    print("=" * 60)
    
    # Sample processed records
    sample_records = [
        {
            'id': 'EXAM_00001',
            'raw_text': 'Lớp K65-A Điểm thi GDTC: 7.5',
            'cleaned_text': 'Lớp K65-A Điểm thi GDTC 7.5',
            'course_code': 'GDTC',
            'course_name': 'Giáo Dục Thể Chất',
            'class_name': 'K65-A',
            'semester_info': {'year': 2022, 'semester': 1},
            'raw_score_text': 'Điểm thi GDTC: 7.5',
            'processed_score': 7.5,
            'source_url': 'https://ptit.edu.vn/...',
            'processed_date': datetime.now().isoformat()
        },
        {
            'id': 'EXAM_00002',
            'raw_text': 'K65-B Triết học Điểm: 8.2/10',
            'cleaned_text': 'K65-B Triết học Điểm 8.2 10',
            'course_code': 'TRIET',
            'course_name': 'Triết Học',
            'class_name': 'K65-B',
            'semester_info': {'year': 2022, 'semester': 1},
            'raw_score_text': 'Điểm: 8.2/10',
            'processed_score': 8.2,
            'source_url': 'https://ptit.edu.vn/...',
            'processed_date': datetime.now().isoformat()
        },
        {
            'id': 'EXAM_00003',
            'raw_text': 'K66-01 Tiếng Anh 6.8 marks',
            'cleaned_text': 'K66-01 Tiếng Anh 6.8 marks',
            'course_code': 'TANH',
            'course_name': 'Tiếng Anh',
            'class_name': 'K66-01',
            'semester_info': {'year': 2022, 'semester': 1},
            'raw_score_text': 'Tiếng Anh 6.8 marks',
            'processed_score': 6.8,
            'source_url': 'https://ptit.edu.vn/...',
            'processed_date': datetime.now().isoformat()
        }
    ]
    
    # Save data
    persistence = DataPersistence()
    
    print("\n✓ Saving data...")
    result = persistence.save_both(sample_records)
    
    print(f"\n✓ Successfully saved {result['total_records']} exam records")
    print(f"\n📄 Generated Files:")
    print(f"   JSON: {result['json']}")
    print(f"   CSV:  {result['csv']}")
    
    # Display file contents
    print("\n" + "=" * 60)
    print("JSON FILE CONTENT (First 2 records):")
    print("=" * 60)
    records = persistence.load_from_json()
    for record in records[:2]:
        print(json.dumps(record, ensure_ascii=False, indent=2))
    
    print("\n" + "=" * 60)
    print("CSV FILE CONTENT (First 3 rows):")
    print("=" * 60)
    csv_records = persistence.load_from_csv()
    if csv_records:
        print("\nHeaders:", ", ".join(csv_records[0].keys()))
        for record in csv_records[:3]:
            print(record)
