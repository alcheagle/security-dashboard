function drawCiambella(datas){
    console.log("Ciao");
    console.log(datas);
    data = {
        datasets: [{
            data : datas,

            backgroundColor: ['rgba(42, 153, 209, 1)',
                'rgba(193, 9, 9 ,1)',
            ]
        }],

        // These labels appear in the legend and in the tooltips when hovering different arcs
        labels: name
    };
    var ctx = document.getElementById("myChart").getContext('2d');
    var myPieChart = new Chart(ctx,{
        type: 'pie',
        data: data,
        options: Chart.defaults.doughnut
    });
}

function runScript(e) {
    if (e.keyCode == 13) {
        $site = $('#inputVal').val();
        console.log($site);

        // window.location = "scan?site="+$someInput;
        $.ajax({
            //the url to send the data to
            url: "scan",
            //the data to send to
            data: {site : $site},
            //type. for eg: GET, POST
            type: "GET",
            //datatype expected to get in reply form server
            dataType: "json",
            //on success
            success: function(data){
                //do something after something is recieved from php
            },
            //on error
            error: function(error){
                // debugger;
            }
        });
    }
}


function sendData(){
    //get the input value
    $site = $('#inputVal').val();
    console.log($site);

    // window.location = "scan?site="+$someInput;
    $.ajax({
        //the url to send the data to
        url: "scan",
        //the data to send to
        data: {site : $site},
        //type. for eg: GET, POST
        type: "GET",
        //datatype expected to get in reply form server
        dataType: "json",
        //on success
        success: function(data){
            //do something after something is recieved from php
        },
        //on error
        error: function(error){
            // debugger;
        }
    });
}
