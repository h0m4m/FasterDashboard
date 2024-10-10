// JavaScript for the car images dropdown
    
// JavaScript for the car images dropdown
const dropdowns = document.querySelectorAll(".dropdown_button");

dropdowns.forEach((dropdown) => {
    dropdown.addEventListener("click", function(e) {
        const content = this.nextElementSibling;
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
        e.stopPropagation(); // Prevents the event from bubbling up
    });
});

// Close dropdown when clicking anywhere outside
document.addEventListener("click", function(e) {
    dropdowns.forEach((dropdown) => {
        const content = dropdown.nextElementSibling;
        if (content.style.display === "block" && !dropdown.contains(e.target)) {
            content.style.display = "none";
        }
    });
});

const bookingbuttonContainer = document.getElementById('booking_info_button_container');
const bookingcontentContainer = document.getElementById('booking_info_content_cont');

bookingbuttonContainer.addEventListener('click', function() {
        bookingcontentContainer.classList.toggle('show-content');
    });

const tipsbuttonContainer = document.getElementById('tips_info_button_container');
const tipscontentContainer = document.getElementById('tips_info_content_cont');

tipsbuttonContainer.addEventListener('click', function() {
        tipscontentContainer.classList.toggle('show-content');
    });

const carbuttonContainer = document.getElementById('car_info_button_container');
const carcontentContainer = document.getElementById('car_info_content_cont');

carbuttonContainer.addEventListener('click', function() {
        carcontentContainer.classList.toggle('show-content');
    });

const conditionbuttonContainer = document.getElementById('condition_info_button_container');
const conditioncontentContainer = document.getElementById('condition_info_content_cont');

conditionbuttonContainer.addEventListener('click', function() {
        conditioncontentContainer.classList.toggle('show-content');
    })

const depositbuttonContainer = document.getElementById('deposit_info_button_container');
const depositcontentContainer = document.getElementById('deposit_info_content_cont');

depositbuttonContainer.addEventListener('click', function() {
        depositcontentContainer.classList.toggle('show-content');
    })



    document.addEventListener("DOMContentLoaded", function() {
        const exteriorSplide = document.querySelector(".external_pictures_splide");
        const blurContainer = document.querySelector(".blur-container");
        const contentContainer = document.querySelector("#exterior_content_container");
        const closeButton = document.querySelector("#splide_exterior_closing_button");
        
        // Show/hide exterior pictures when clicking the content container
        contentContainer.addEventListener("click", () => {
            exteriorSplide.classList.add("show-content");
            blurContainer.classList.add("show-blur"); // Apply blur effect container
            document.body.style.overflow = "hidden"; // Disable scrolling
        });
    
        // Close exterior pictures when clicking the close button
        closeButton.addEventListener("click", (event) => {
            exteriorSplide.classList.remove("show-content");
            blurContainer.classList.remove("show-blur"); // Remove blur effect container
            document.body.style.overflow = ""; // Enable scrolling
            console.log("hi");
            event.stopPropagation(); // Prevent the event from propagating further
        });
    
        // Close exterior pictures when clicking anywhere outside the container
        document.addEventListener("click", (event) => {
            if (!event.target.closest('.interior_and_exterior_content_container')) {
                exteriorSplide.classList.remove("show-content");
                blurContainer.classList.remove("show-blur"); // Remove blur effect container
                document.body.style.overflow = ""; // Enable scrolling
            }
        });

        const interiorSplide = document.querySelector(".interior_pictures_splide");
        const interiorcontentContainer = document.querySelector("#interior_content_container");
        const interiorcloseButton = document.querySelector("#splide_interior_closing_button");
        
        // Show/hide exterior pictures when clicking the content container
        interiorcontentContainer.addEventListener("click", () => {
            interiorSplide.classList.add("show-content");
            blurContainer.classList.add("show-blur"); // Apply blur effect container
            document.body.style.overflow = "hidden"; // Disable scrolling
        });
    
        // Close exterior pictures when clicking the close button
        interiorcloseButton.addEventListener("click", (event) => {
            interiorSplide.classList.remove("show-content");
            blurContainer.classList.remove("show-blur"); // Remove blur effect container
            document.body.style.overflow = ""; // Enable scrolling
            console.log("hi");
            event.stopPropagation(); // Prevent the event from propagating further
        });
    
        // Close exterior pictures when clicking anywhere outside the container
        document.addEventListener("click", (event) => {
            if (!event.target.closest('.interior_and_exterior_content_container')) {
                interiorSplide.classList.remove("show-content");
                blurContainer.classList.remove("show-blur"); // Remove blur effect container
                document.body.style.overflow = ""; // Enable scrolling
            }
        });
    });
    
    let table = new DataTable('#finesTable', {
        // options
    });
    
    


































