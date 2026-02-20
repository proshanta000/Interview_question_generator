document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const btn = document.querySelector('button');
    const fileInput = document.querySelector('input[type="file"]');

    form.addEventListener('submit', (e) => {
        // 1. Basic Validation
        if (fileInput.files.length === 0) {
            alert("Please select a PDF file first!");
            e.preventDefault();
            return;
        }

        // 2. Change button state to "Loading"
        btn.innerHTML = `<span class="spinner"></span> Processing with AI...`;
        btn.style.opacity = "0.7";
        btn.style.pointerEvents = "none";

        // 3. Show a console log for debugging
        console.log("PDF Uploaded. Starting Generation Pipeline...");
    });
});