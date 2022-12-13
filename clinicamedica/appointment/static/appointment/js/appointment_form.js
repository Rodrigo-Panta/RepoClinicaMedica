

document.addEventListener("DOMContentLoaded", function(e) { 
    document.getElementById('id_specialty').addEventListener('change', updateDoctorField);
    updateDoctorField();


});

function updateDoctorField(event){
    let specialty = document.getElementById('id_specialty').value;
    let doctor_field = document.getElementById('id_doctor');
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
    doctors.forEach(element => {
        doctor_field.innerHTML += `\n<option value="">${element}</option>`;    
    });
    doctor_field.disabled = false;
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