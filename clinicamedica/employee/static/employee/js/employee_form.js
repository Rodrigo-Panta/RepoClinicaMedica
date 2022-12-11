document.addEventListener("DOMContentLoaded", function(e) { 
    document.getElementById('id_is_doctor').addEventListener('change', toggleDoctorForm);
    toggleDoctorForm();
  });

function toggleDoctorForm(){
    let checkbox = document.getElementById('id_is_doctor');
    let crm_input = document.getElementById("id_crm");
    let specialty_input = document.getElementById("id_specialty");
    if(checkbox.checked){
        crm_input.closest(".form-group").style.visibility = 'visible';
        specialty_input.closest(".form-group").style.visibility = 'visible';
        crm_input.required = true;
        specialty_input.required = true;

    } else {
        crm_input.closest(".form-group").style.visibility = 'hidden';
        specialty_input.closest(".form-group").style.visibility = 'hidden';
        crm_input.required = false;
        specialty_input.required = false;
    }
    console.log(value);
}

