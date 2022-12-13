

document.addEventListener("DOMContentLoaded", function(e) { 
        document.getElementById('id_specialty').addEventListener('change', updateDoctorField);
    updateDoctorField();
    
    document.getElementById('id_doctor').addEventListener('change', updateTimeField);
    document.getElementById('id_date').addEventListener('change', updateTimeField);
    updateTimeField();


});

function updateDoctorField(event){
    let specialty = document.getElementById('id_specialty').value;
    let doctor_field = document.getElementById('id_doctor');
    doctor_field.innerHTML = '';
    if(specialty){
        url = `${document.getElementById('api_get_doctors_url').value}${specialty}`;
        httpGetAsync(url, populateDoctorField);
    }else{
        doctor_field.disabled = true;
        doctor_field.innerHTML = '<option value="" selected="">-------------</option>';
    }

}

function populateDoctorField(doctorsString){
    let doctorsResponse = JSON.parse(doctorsString);
    let doctors = doctorsResponse['doctors'];
    let doctor_field = document.getElementById('id_doctor');
    for (key in doctors) {
        doctor_field.innerHTML += `\n<option value="${key}">${doctors[key]}</option>`;    
    }
    doctor_field.disabled = false;
}   


function updateTimeField(event){
    let doctor = document.getElementById('id_doctor').value;
    let date = document.getElementById('id_date').value;
    let time_field = document.getElementById('id_time');
    if(doctor && date){

        url = `${document.getElementById('api_get_available_times_url').value}${doctor}/${date.replaceAll('/','_')}`;
        httpGetAsync(url,populateTimeField);
      }else{
        time_field.disabled = true;
        time_field.innerHTML = '<option value="" selected="">-------------</option>';
    }

}

function populateTimeField(timeString){
    console.log(timeString);
    let timeResponse = JSON.parse(timeString);
    let available_times = timeResponse['times'];
    let time_field = document.getElementById('id_time');
    available_times.forEach(element => {
        time_field.innerHTML += `\n<option value="">${element}</option>`;    
    });
    time_field.disabled = false;
}   



function httpGetAsync(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}

