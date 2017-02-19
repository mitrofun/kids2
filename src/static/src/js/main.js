// popup delete form
(function () {
    if (document.readyState||document.body.readyState=='complete'){

    window.obj_delete = function(obj_name, del_url)
    {
        document.getElementById("object").innerHTML ='Удалить ' + obj_name + '?';
        document.delete_form.action = del_url;
    };
}
})();

// select2 widget
(function () {
    if (document.readyState||document.body.readyState=='complete'){
         $('select').select2();
    }
})();

// bootstrap-datepicker widget
(function () {
    if (document.readyState||document.body.readyState=='complete'){
        $('#id_birthday').datepicker({
            language: "ru",
            clearBtn: true,
            autoclose: true
        });
        $('#id_first_date').datepicker({
            language: "ru",
            clearBtn: true,
            todayBtn: "linked",
            autoclose: true
        });
        $('#id_last_date').datepicker({
            language: "ru",
            clearBtn: true,
            todayBtn: "linked",
            autoclose: true
        });
        $('#id_load_date').datepicker({
            language: "ru",
            clearBtn: true,
            todayBtn: "linked",
            autoclose: true
        });
        $('#id_report_date').datepicker({
            language: "ru",
            clearBtn: true,
            todayBtn: "linked",
            autoclose: true
        });
    }
})();

// datatables

(function () {
    if (document.readyState||document.body.readyState=='complete'){
        $('#children').DataTable( {
            "aLengthMenu": [[25, 50, 75, 100, -1], [25, 50, 75, 100, "Все"]],
            "iDisplayLength": 100,
            'scrollY': '50vh',
            'scrollCollapse': true,
            'processing': true,
            'serverSide': true,
            'stateSave': true,
            'columns': [
                { 'data': 'full_name' ,
                    "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
            $(nTd).html("<a href='"+oData.link+"'>"+oData.full_name+"</a>");
                    }
                },
                { 'data': 'age' }
                ],
            'ajax': '/children/data-table/',
            'language': {
                'url': '../static/src/json/dataTables.ru.json'
            }
        }
        );
    }
})();

(function () {
    $('input[type=file]').bootstrapFileInput();
})();

(function () {
    setTimeout(function() {$(".alert").fadeOut()}, 2000);
})();

// slug

(function () {
    if (document.readyState||document.body.readyState=='complete'){
        $("#id_name").keyup(function(){
        var Text = $(this).val();
        Text = slugify(Text);
        $("#id_slug").val((Text));
});
    }
})();

// report filter

(function () {
    if (document.readyState||document.body.readyState=='complete') {

        var $eventSelect = $("#id_report_type"),
            $institutionSelect = $("#id_institution"),
            $groupSelect = $("#id_group"),
            $gradeSelect = $("#id_grade"),
            $healthStatesSelect = $("#id_health_states"),
            $modeHealthStatesRadio = $("#id_mode_health_states_0"),
            $parentsStatusSelect = $("#id_parents_status"),
            $modeParentsStatusRadio = $("#id_mode_parents_status_0");

        $eventSelect.on("change", function (e) {

            if ($eventSelect[0].value === '2'){
                $institutionSelect[0].parentNode.parentNode.classList.add('is_hide');
                $groupSelect[0].parentNode.parentNode.classList.add('is_hide');
                $gradeSelect[0].parentNode.parentNode.classList.add('is_hide');
                $healthStatesSelect[0].parentNode.parentNode.classList.add('is_hide');
                $modeHealthStatesRadio[0].parentNode.parentNode.parentElement.parentElement.classList.add('is_hide');
                $parentsStatusSelect[0].parentNode.parentNode.classList.add('is_hide');
                $modeParentsStatusRadio[0].parentNode.parentNode.parentElement.parentElement.classList.add('is_hide');
            } else {
                $institutionSelect[0].parentNode.parentNode.classList.remove('is_hide');
                $groupSelect[0].parentNode.parentNode.classList.remove('is_hide');
                $gradeSelect[0].parentNode.parentNode.classList.remove('is_hide');
                $healthStatesSelect[0].parentNode.parentNode.classList.remove('is_hide');
                $modeHealthStatesRadio[0].parentNode.parentNode.parentElement.parentElement.classList.remove('is_hide');
                $parentsStatusSelect[0].parentNode.parentNode.classList.remove('is_hide');
                $modeParentsStatusRadio[0].parentNode.parentNode.parentElement.parentElement.classList.remove('is_hide');
            }

        });

    }
})();
