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

        var table = $('#children').DataTable( {
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
        });

        var date = document.getElementById('id_report_date'),
            institution = document.getElementById('id_institution'),
            group = document.getElementById('id_group'),
            grade = document.getElementById('id_grade'),
            healthStates = document.getElementById('id_health_states'),
            healthStatesMode = document.getElementsByName('mode_health_states'),
            parentsStatus = document.getElementById('id_parents_status'),
            parentsStatusMode = document.getElementsByName('mode_parents_status'),
            btnFilter = document.getElementById('btnFilter'),
            btnReset = document.getElementById('btnReset');

        function getSelectValues(select) {
            var result = [];
            var options = select && select.options;
            var opt;

            for (var i=0; i<options.length; i++) {
                opt = options[i];

                if (opt.selected) {
                  result.push(opt.value || opt.text);
                }
              }
            return result;
        }

        function getCheckedValues(radio) {
            var result = 0;

            for (var i=0; i < radio.length; i++) {
                if (radio[i].checked) {
                    result = i;
                }
            }

            return result;
        }

        function applyFilter() {
            // console.log('filter');
            var searchText = {};
            if (institution.value) {
                searchText['institution'] = parseInt(institution.value);
            }
            if (group.value) {
                searchText['group'] = parseInt(group.value);
            }
            if (grade.value) {
                searchText['grade'] = parseInt(grade.value);
            }
            if (healthStates.value) {
                searchText['health_states'] = getSelectValues(healthStates);
                searchText['mode_health_states'] = getCheckedValues(healthStatesMode);
            }
            if (parentsStatus.value) {
                searchText['parents_status'] = getSelectValues(parentsStatus);
                searchText['mode_parents_status'] = getCheckedValues(parentsStatusMode);
            }

            if (date.value) {
                var dateArray = date.value.split('.');
                searchText['date'] = new Date (dateArray[2], dateArray[1], dateArray[0]);
            }

            // console.log(searchText);

            table.columns(0).search(JSON.stringify(searchText));
            localStorage.setItem("filter_" + window.location.pathname, JSON.stringify(searchText));
            table.draw();

        }

        function resetFilter() {
            // console.log('reset');

            $("#id_institution").select2().val('').change();
            $("#id_group").select2().val('').change();
            $("#id_grade").select2().val('').change();
            $("#id_health_states").select2().val('').change();
            $("#id_parents_status").select2().val('').change();

            healthStatesMode[0].checked = true;
            parentsStatusMode[0].checked = true;
            table.columns(0).search('');
            localStorage.clear("filter_" + window.location.pathname);
            table.draw();

        }
        if (btnFilter) {btnFilter.addEventListener('click', applyFilter );}
        if (btnReset) {btnReset.addEventListener('click',resetFilter );}

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
            $gradeSelect = $("#id_grade");

        $eventSelect.on("change", function (e) {

            if ($eventSelect[0].value === '2'){
                $institutionSelect[0].parentNode.parentNode.classList.add('is_hide');
                $groupSelect[0].parentNode.parentNode.classList.add('is_hide');
                $gradeSelect[0].parentNode.parentNode.classList.add('is_hide');

            } else {
                $institutionSelect[0].parentNode.parentNode.classList.remove('is_hide');
                $groupSelect[0].parentNode.parentNode.classList.remove('is_hide');
                $gradeSelect[0].parentNode.parentNode.classList.remove('is_hide');
            }

        });

    }
})();

// page loader
(function () {
    $(window).load(function() {
        // console.log('load');
        var pageLoader = document.getElementById('page-loader'),
            spinner = document.getElementsByClassName('spinner')[0];
        spinner.classList.add('is_hide');
        pageLoader.classList.add('is_hide');
    });
})();


// init filter field
(function () {
    if (document.readyState||document.body.readyState=='complete'){

        function padWithZeroes(number, length) {
            var myString = '' + number;
            while (myString.length < length) {
                myString = '0' + myString;
            }

            return myString;
        }

        var filterParams = JSON.parse(localStorage.getItem("filter_" + window.location.pathname));
        var healthStatesMode = document.getElementsByName('mode_health_states'),
            parentsStatusMode = document.getElementsByName('mode_parents_status');

        // console.log(filterParams);

        if (filterParams) {
            if ('date' in filterParams) {
                var date = new Date(filterParams['date']);
                var month = padWithZeroes(date.getMonth(), 2);
                var day = padWithZeroes(date.getDate(), 2);
                var strDate = `${day}.${month}.${date.getFullYear()}`;
                $('#id_report_date').val(strDate).change()
            }

            if ('institution' in filterParams) {
                $("#id_institution").select2().val(filterParams['institution']).change();
            }
            if ('group' in filterParams) {
                $("#id_group").select2().val(filterParams['group']).change();
            }
            if ('grade' in filterParams) {
                $("#id_grade").select2().val(filterParams['grade']).change();
            }
            if ('health_states' in filterParams) {
                $("#id_health_states").select2().val(filterParams['health_states']).change();
            }
            if ('mode_health_states' in filterParams) {
                if (healthStatesMode.length) {
                    healthStatesMode[parseInt(filterParams['mode_health_states'])].checked = true;
                }
            }
            if ('parents_status' in filterParams) {
                $("#id_parents_status").select2().val(filterParams['parents_status']).change();
            }
            if ('mode_parents_status' in filterParams) {
                if (parentsStatusMode.length) {
                    parentsStatusMode[parseInt(filterParams['mode_parents_status'])].checked = true;
                }

            }

        }
    }
})();

// status report load
(function () {

    var jobPopup = document.getElementsByClassName('job')[0],
        jobName = document.getElementsByClassName('job__name')[0],
        jobLoader = document.getElementsByClassName('job__loader')[0],
        jobResult = document.getElementsByClassName('job__result')[0],
        jobLink = document.getElementById('jobLink'),
        task;

    function readCookie(name) {
        var nameEQ = name + "=";
        var ca = document.cookie.split(';');
        for(var i=0;i < ca.length;i++) {
            var c = ca[i];
            while (c.charAt(0)==' ') c = c.substring(1,c.length);
            if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
        }
    return null;
    }


    function deleteCookie(name) {
        document.cookie = name +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
    }

    function getNameTask(task) {

        var result;
        if (task === '1') {
            result = 'Формирование отчета' }
        else {
            result = 'Загрузка данных'
        }
        return result;
    }

    function show_status(data) {
        if (data.status === "failed") {
            // console.log(data.status);
            clearInterval(intervalID);
            jobName.innerHTML = 'Ошибка формирования';
            deleteCookie('kids_report_job');
            deleteCookie('kids_job_task');
        }
        if (data.status === "waiting"){
            // do nothing
            // console.log(data.status);
        }
        else if (data.status === "finished"){
            // console.log(data.status);
            if (task === '1') {
                jobName.innerHTML = 'Отчет сформирован';
                jobLoader.style.display = 'none';
                jobLink.href = '/reports/get/?job_id=' + job;
                jobResult.style.display = 'block';
            } else {
                jobName.innerHTML = 'Данные загружены';
                jobLoader.style.display = 'none';
                deleteCookie('kids_loader_job');
                deleteCookie('kids_job_task');
                setTimeout(function () {
                    jobPopup.style.display='none'
                }, 2500);
            }
            clearInterval(intervalID);
        }
        else {
            // console.log(data.status);
            clearInterval(intervalID);
        }
    }

    function handle_error(xhr, textStatus, errorThrown) {
        console.log("Please report this error: "+errorThrown+xhr.status+xhr.responseText);
    }

    function check_status() {
        var sendID = '';

        if (task === '1') {
            sendID = job;
        } else {
            sendID = jobCookeLoader;
        }

        $.ajax({
            type: "GET",
            url: "/status/?job_id=" + sendID,
            success: show_status,
            error: handle_error
        });
    }

    if (document.readyState||document.body.readyState=='complete'){
        var job = readCookie('kids_report_job'),
            jobCookeLoader = readCookie('kids_loader_job'),
            intervalID;

        task = readCookie('kids_job_task');
        var nameTask = getNameTask(task);
        // console.log(job);
        if (job || jobCookeLoader)  {
            console.log('loading');
            console.log(task);

            jobPopup.style.display = 'block';
            jobName.innerHTML = nameTask;

            setTimeout(check_status, 0.05);
            intervalID = setInterval(check_status, 1000);
        }
    }

    jobLink.addEventListener('click', function () {
        jobPopup.style.display = 'none';
        deleteCookie('kids_report_job');
        deleteCookie('kids_job_task');
    })

})();
