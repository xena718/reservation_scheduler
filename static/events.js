
document.getElementById('datePicker').valueAsDate = new Date();


function createOption(value, text) {
    const option = document.createElement('option');
    option.text = text;
    option.value = value;
    return option;
}

const hourSelectAll = document.querySelectorAll('.hours');
for (const hourSelect of hourSelectAll) {

for(let i = 0; i <= 12; i++){
        hourSelect.add(createOption(i, i));
}
}

const minutesSelectAll = document.querySelectorAll('.minutes');
for(const minutesSelect of minutesSelectAll){
for(let i = 0; i < 60; i += 30) {
        minutesSelect.add(createOption(i, i));
}
}

