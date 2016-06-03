if(document.readyState||document.body.readyState=='complete'){
    // alert('YES!');

    window.obj_delete = function(obj_name, del_url)
    {
        document.getElementById("object").innerHTML ='Удалить ' + obj_name + '?';
        document.delete_form.action = del_url;
    }
}
