document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const tableBody = document.querySelector('table tbody');

    // 1. Handle Form Submission (Add Student)
    form.addEventListener('submit', (event) => {
        // Prevent the page from refreshing on form submit
        event.preventDefault();

        // Grab form values
        const studentId = document.getElementById('studentId').value.trim();
        const fullName = document.getElementById('fullName').value.trim();
        const email = document.getElementById('email').value.trim();
        const courseSelect = document.getElementById('course');
        const courseText = courseSelect.options[courseSelect.selectedIndex].text;

        // Create a new row
        const newRow = document.createElement('tr');

        // Populate the row with student data
        newRow.innerHTML = `
            <td>${studentId}</td>
            <td>${fullName}</td>
            <td>${email}</td>
            <td>${courseText}</td>
            <td><button class="yusa">Delete</button></td>
        `;

        // Append the new row to the table body
        tableBody.appendChild(newRow);

        // Reset the form fields
        form.reset();
    });

    // 2. Handle Deletion (Event Delegation)
    // This works for both the hardcoded row and any new rows you add!
    tableBody.addEventListener('click', (event) => {
        // Check if the clicked element is a delete button
        if (event.target.classList.contains('yusa')) {
            const row = event.target.closest('tr');
            
            // Optional: Add a confirmation dialog before deleting
            if (confirm('Are you sure you want to delete this student record?')) {
                row.remove();
            }
        }
    });
});