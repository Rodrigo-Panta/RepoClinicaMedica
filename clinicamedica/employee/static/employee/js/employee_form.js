document.addEventListener("DOMContentLoaded", function(e) { 
    document.getElementById('id_is_doctor').addEventListener('change', updateDoctorForm);
    updateDoctorForm();

    document.getElementById('id_cep').addEventListener('keyup', searchAddress);

});

function updateDoctorForm(event){
    let checkbox = document.getElementById('id_is_doctor');
    let crm_input = document.getElementById("id_crm");
    let specialty_input = document.getElementById("id_specialty");
    if(checkbox.checked){
        crm_input.closest("div").style.visibility = 'visible';
        specialty_input.closest("div").style.visibility = 'visible';
        crm_input.required = true;
        specialty_input.required = true;

    } else {
        crm_input.closest("div").style.visibility = 'hidden';
        specialty_input.closest("div").style.visibility = 'hidden';
        crm_input.required = false;
        specialty_input.required = false;
    }
}

function searchAddress(event){
    let value = document.getElementById('id_cep').value;
    
    if(value.length == 8){
        setTimeout(() => {
            let url = document.getElementById('api_get_address_url').value + value;
            httpGetAsync(url, updateAddress);
        }, "500")

    }

}

function updateAddress(address_str){
    if(address_str){
        let address = JSON.parse(address_str);
        for(key in address){
            document.getElementById(`id_${key}`).value = address[key];  
        }
    }
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