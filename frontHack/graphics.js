

function drawCiambella(){
        data = {
        datasets: [{
            data: [80, 20],

            backgroundColor: ['rgba(42, 153, 209, 1)',
                'rgba(193, 9, 9 ,1)',
              ]
        }],

        // These labels appear in the legend and in the tooltips when hovering different arcs
        labels: [
            'Http',
            'Https',
        ],
      };
      var ctx = document.getElementById("myChart").getContext('2d');
      var myPieChart = new Chart(ctx,{
      type: 'pie',
      data: data,
      options: Chart.defaults.doughnut
      });

}


function sendData(){
        //get the input value
        $someInput = $('#inputVal').val();
        console.log($someInput);
        window.location = "result.html";
        /*$.ajax({
            //the url to send the data to
            url: "ajax/url.ajax.php",
            //the data to send to
            data: {someInput : $someInput},
            //type. for eg: GET, POST
            type: "GET",
            //datatype expected to get in reply form server
            dataType: "json",
            //on success
            success: function(data){
                //do something after something is recieved from php
            },
            //on error
            error: function(){
                //bad request
            }
        });*/
    }
