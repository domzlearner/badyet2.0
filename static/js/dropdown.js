// Function to dynamically generate the year options
function populateYearOptions() {
    const yearSelect = document.getElementById('year');
    const currentYear = new Date().getFullYear();

    for (let i = 0; i < 5; i++) {  // Generate years from current year to 4 years in the future
        const yearOption = document.createElement('option');
        yearOption.value = currentYear + i;
        yearOption.text = currentYear + i;
        yearSelect.appendChild(yearOption);
    }
}

// Function to calculate and update the date range
function updateDateRange() {
    const month = document.getElementById('month').value;
    const year = document.getElementById('year').value;

    const startDate = new Date(year, month - 1, 1);
    const endDate = new Date(year, month, 0);

    const startStr = startDate.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
    const endStr = endDate.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });

    document.getElementById('date-range').innerText = `Start Date: ${startStr} - End Date: ${endStr}`;
}

// Initialize with the current date and populate year options when the page loads
window.onload = function() {
    populateYearOptions();
    updateDateRange();
};
