/**
 * Student Academic Portal - JavaScript
 * Handles client-side interactions and dynamic content
 */

// DOM Ready
document.addEventListener('DOMContentLoaded', function() {
    console.log('Student Portal loaded');
    initializeCharts();
});

/**
 * Initialize all charts on the page
 */
function initializeCharts() {
    // Chart.js is loaded globally
    if (typeof Chart !== 'undefined') {
        console.log('Chart.js library is available');
    }
}

/**
 * Format number as percentage
 */
function formatPercentage(value) {
    return parseFloat(value).toFixed(2) + '%';
}

/**
 * Format number with 2 decimal places
 */
function formatNumber(value) {
    return parseFloat(value).toFixed(2);
}

/**
 * Get grade color based on score
 */
function getGradeColor(score) {
    if (score >= 90) return '#28a745';  // Green
    if (score >= 80) return '#007bff';  // Blue
    if (score >= 70) return '#ffc107';  // Yellow
    if (score >= 60) return '#fd7e14';  // Orange
    return '#dc3545';  // Red
}

/**
 * Get grade letter
 */
function getLetterGrade(score) {
    if (score >= 90) return 'A';
    if (score >= 80) return 'B';
    if (score >= 70) return 'C';
    if (score >= 60) return 'D';
    return 'F';
}

/**
 * Create a bar chart
 */
function createBarChart(canvasId, labels, data, title = '') {
    if (!document.getElementById(canvasId)) return;

    const ctx = document.getElementById(canvasId).getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: title,
                data: data,
                backgroundColor: 'rgba(54, 162, 235, 0.8)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100
                }
            }
        }
    });
}

/**
 * Create a line chart
 */
function createLineChart(canvasId, labels, data, title = '') {
    if (!document.getElementById(canvasId)) return;

    const ctx = document.getElementById(canvasId).getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: title,
                data: data,
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.1)',
                tension: 0.3,
                fill: true
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100
                }
            }
        }
    });
}

/**
 * Create a pie chart
 */
function createPieChart(canvasId, labels, data, title = '') {
    if (!document.getElementById(canvasId)) return;

    const ctx = document.getElementById(canvasId).getContext('2d');
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: [
                    'rgba(75, 192, 192, 0.8)',
                    'rgba(54, 162, 235, 0.8)',
                    'rgba(255, 206, 86, 0.8)',
                    'rgba(153, 102, 255, 0.8)',
                    'rgba(255, 159, 64, 0.8)'
                ]
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
}

/**
 * Fetch and display course grades
 */
async function loadCourseGrades(courseId) {
    try {
        const response = await fetch(`/api/course-stats/${courseId}`);
        const data = await response.json();
        console.log('Course stats:', data);
        return data;
    } catch (error) {
        console.error('Error loading course grades:', error);
    }
}

/**
 * Fetch and display student trend
 */
async function loadStudentTrend(studentId) {
    try {
        const response = await fetch(`/api/student-trend/${studentId}`);
        const data = await response.json();
        console.log('Student trend:', data);
        return data;
    } catch (error) {
        console.error('Error loading student trend:', error);
    }
}

/**
 * Fetch at-risk students
 */
async function loadAtRiskStudents() {
    try {
        const response = await fetch('/api/at-risk-students');
        const data = await response.json();
        console.log('At-risk students:', data);
        return data;
    } catch (error) {
        console.error('Error loading at-risk students:', error);
    }
}

/**
 * Fetch top performers
 */
async function loadTopPerformers() {
    try {
        const response = await fetch('/api/top-performers');
        const data = await response.json();
        console.log('Top performers:', data);
        return data;
    } catch (error) {
        console.error('Error loading top performers:', error);
    }
}

/**
 * Show toast notification
 */
function showToast(message, type = 'info') {
    const toastContainer = document.getElementById('toastContainer');
    if (!toastContainer) return;

    const toast = document.createElement('div');
    toast.className = `alert alert-${type} alert-dismissible fade show`;
    toast.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    toastContainer.appendChild(toast);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        toast.remove();
    }, 5000);
}

/**
 * Format date string
 */
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
    });
}

/**
 * Format time string
 */
function formatTime(dateString) {
    const date = new Date(dateString);
    return date.toLocaleTimeString('en-US', {
        hour: '2-digit',
        minute: '2-digit'
    });
}

/**
 * Validate email address
 */
function validateEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

/**
 * Export table to CSV
 */
function exportTableToCSV(tableId, filename = 'export.csv') {
    const table = document.getElementById(tableId);
    if (!table) return;

    let csv = [];
    const rows = table.querySelectorAll('tr');
    
    rows.forEach(row => {
        const cols = row.querySelectorAll('td, th');
        const csvRow = [];
        cols.forEach(col => {
            csvRow.push(col.textContent);
        });
        csv.push(csvRow.join(','));
    });

    downloadCSV(csv.join('\n'), filename);
}

/**
 * Download CSV file
 */
function downloadCSV(csv, filename) {
    const link = document.createElement('a');
    link.href = 'data:text/csv;charset=utf-8,' + encodeURIComponent(csv);
    link.download = filename;
    link.click();
}

/**
 * Print page
 */
function printPage() {
    window.print();
}

/**
 * Add animation to elements
 */
function addFadeInAnimation(element) {
    element.classList.add('fade-in');
}

/**
 * Global error handler
 */
window.addEventListener('error', function(event) {
    console.error('Global error:', event.error);
});

/**
 * Detect dark mode preference
 */
function isDarkModeEnabled() {
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
}

/**
 * Initialize tooltips (if using Bootstrap)
 */
function initializeTooltips() {
    if (typeof bootstrap !== 'undefined') {
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
}

// Initialize tooltips on load
document.addEventListener('DOMContentLoaded', initializeTooltips);

console.log('Student Portal JavaScript loaded successfully');
