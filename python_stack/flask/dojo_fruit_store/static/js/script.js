function getDaySuffix(day) {
    if (day >= 11 && day <= 13) return "th";
    switch (day % 10) {
        case 1: return "st";
        case 2: return "nd";
        case 3: return "rd";
        default: return "th";
    }
}

const now = new Date();

// Month (March)
const month = now.toLocaleString('en-US', { month: 'long' });

// Day + suffix (23rd)
const day = now.getDate();
const suffix = getDaySuffix(day);

// Year
const year = now.getFullYear();

// Time
let hours = now.getHours();
const minutes = String(now.getMinutes()).padStart(2, '0');
const seconds = String(now.getSeconds()).padStart(2, '0');

// AM / PM
const ampm = hours >= 12 ? "PM" : "AM";
hours = hours % 12 || 12;

// Final format
const formatted = `${month} ${day}${suffix} ${year} ${hours}:${minutes}:${seconds} ${ampm}`;

// Display in HTML
document.getElementById("date").textContent = formatted;