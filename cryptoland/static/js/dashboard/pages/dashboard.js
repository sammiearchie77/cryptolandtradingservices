//[Dashboard Javascript]

//Project:	Crypto Admin - Responsive Admin Template
//Primary use:   Used only for the main dashboard (index.html)


$(function () {

  'use strict'; 
	

	//Trafic Chart
    if ($("#doughnut-chart").length) {
      var ctx = document.getElementById('doughnut-chart').getContext("2d");

      var gradientStrokeBlue = ctx.createLinearGradient(0, 0, 0, 181);
      gradientStrokeBlue.addColorStop(0, '#3600e8');
      gradientStrokeBlue.addColorStop(1, '#5730d5');
      var gradientLegendBlue = 'linear-gradient(145deg, #3600e8, #5730d5)';

      var gradientStrokeRed = ctx.createLinearGradient(0, 0, 0, 150);
      gradientStrokeRed.addColorStop(0, '#9152e1');
      gradientStrokeRed.addColorStop(1, '#101aec');
      var gradientLegendRed = 'linear-gradient(145deg, #9152e1, #101aec)';

      var gradientStrokeParple = ctx.createLinearGradient(0, 0, 0, 150);
      gradientStrokeParple.addColorStop(0, '#ff5858');
      gradientStrokeParple.addColorStop(1, '#38b8f2');
      var gradientLegendParple = 'linear-gradient(145deg, #ff5858, #38b8f2)';

      var doughnutChartData = {
        datasets: [{
          data: [70, 50],
          backgroundColor: [
            gradientStrokeBlue,
            gradientStrokeRed,
			gradientStrokeParple,
          ],
          hoverBackgroundColor: [  
			gradientStrokeBlue,          
            gradientStrokeRed,
			gradientStrokeParple,
          ],
          borderColor: [
            gradientStrokeBlue,
            gradientStrokeRed,
			gradientStrokeParple,
          ],
          legendColor: [
            gradientLegendBlue,
            gradientLegendRed,
			gradientLegendParple,
          ]
        }],
    
        // These labels appear in the legend and in the tooltips when hovering different arcs
        labels: [
          'Facebook',
          'Google',
          'Linkedin',
        ]
      };
      var doughnutChartOptions = {
        responsive: true,
        animation: {
          animateScale: true,
          animateRotate: true
        },
        legend: false,
        legendCallback: function(chart) {
          var text = []; 
          text.push('<ul>'); 
          for (var i = 0; i < doughnutChartData.datasets[0].data.length; i++) { 
              text.push('<li><h2 class="mb-2">'+doughnutChartData.datasets[0].data[i]+'%</h2><div class="legend-content"><span class="legend-dots" style="background:' + 
              doughnutChartData.datasets[0].legendColor[i] + 
                          '"></span>'+doughnutChartData.labels[i]+'</div>'); 
              text.push('</li>'); 
          }
          text.push('</ul>'); 
          return text.join('');
        },
        cutoutPercentage: 95
      };
      var doughnutChartPlugins = {
        beforeDraw: function(chart) {
          var width = chart.chart.width,
              height = chart.chart.height,
              ctx = chart.chart.ctx;			
      
          ctx.restore();
          var fontSize = 1.2;
          ctx.font = fontSize + "em sans-serif";
          ctx.textBaseline = "middle";
          ctx.fillStyle = "#ffffff";
      	  ctx.fill = function() {
				ctx.save();
				ctx.shadowColor = 'yellow';
				ctx.shadowBlur = 5;
				ctx.shadowOffsetX = 2;
				ctx.shadowOffsetY = 2;
				_fill.apply(this, arguments)
				ctx.restore();
			};
          var text = "1.2 M",
              textX = Math.round((width - ctx.measureText(text).width) / 2),
              textY = height / 2;
      
          ctx.fillText(text, textX, textY);
          ctx.save();
        }
      }
      var doughnutChartCanvas = $("#doughnut-chart").get(0).getContext("2d");
      var doughnutChart = new Chart(doughnutChartCanvas, {
        type: 'doughnut',
        data: doughnutChartData,
        options: doughnutChartOptions,
        plugins: doughnutChartPlugins
      });
      $("#doughnut-chart-legend").html(doughnutChart.generateLegend()); 
    }
	


	
	

	
   Morris.Area({
        element: 'area-chart',
        data: [{
            period: '2010',
            data1: 55,
            data2: 85,
            data3: 25
        }, {
            period: '2011',
            data1: 135,
            data2: 105,
            data3: 85
        }, {
            period: '2012',
            data1: 85,
            data2: 65,
            data3: 75
        }, {
            period: '2013',
            data1: 75,
            data2: 205,
            data3: 145
        }, {
            period: '2014',
            data1: 185,
            data2: 155,
            data3: 145
        }, {
            period: '2015',
            data1: 110,
            data2: 105,
            data3: 85
        },
         {
            period: '2016',
            data1: 255,
            data2: 155,
            data3: 205
        }],
        xkey: 'period',
        ykeys: ['data1', 'data2', 'data3'],
        labels: ['Data 1', 'Data 2', 'Data 3'],
        pointSize: 3,
        fillOpacity: 0,
        pointStrokeColors:['#0bb2d4', '#17b3a3', '#3e8ef7'],
        behaveLikeLine: true,
        gridLineColor: '#e0e0e0',
        lineWidth: 3,
        hideHover: 'auto',
        lineColors: ['#f99480', '#2d6bfa', '#c535a4'],
        resize: true
        
    });
	
	
	
  // bootstrap WYSIHTML5 - text editor
  $('.textarea').wysihtml5();	

   
  // SLIMSCROLL FOR CHAT WIDGET
  $('#direct-chat').slimScroll({
    height: '380px'
  });
	
//ticker
 	if ($('#webticker-1').length) {   
		$("#webticker-1").webTicker({
			height:'auto', 
			duplicate:true, 
			startEmpty:false, 
			rssfrequency:5
		});
	}
//data table
    $('#example1').DataTable({
      'paging'      : false,
      'lengthChange': false,
      'searching'   : false,
      'ordering'    : true,
      'info'        : false,
      'autoWidth'   : false
    });
	
}); // End of use strict
