//[Dashboard chart Javascript]

//Project:	Crypto Admin - Responsive Admin Template


 		
//-----amchart
//----------------chartdiv21

var chart = AmCharts.makeChart( "chartdiv21", {
  "type": "stock",
"theme": "black",

  //"color": "#fff",
  "dataSets": [ {
    "title": "MSFT",
    "fieldMappings": [ {
      "fromField": "Open",
      "toField": "open"
    }, {
      "fromField": "High",
      "toField": "high"
    }, {
      "fromField": "Low",
      "toField": "low"
    }, {
      "fromField": "Close",
      "toField": "close"
    }, {
      "fromField": "Volume",
      "toField": "volume"
    } ],
    "compared": false,
    "categoryField": "Date",

    /**
     * data loader for data set data
     */
    "dataLoader": {
      "url": "https://www.amcharts.com/wp-content/uploads/assets/stock/MSFT.csv",
      "format": "csv",
      "showCurtain": true,
      "showErrors": true,
      "async": true,
      "reverse": true,
      "delimiter": ",",
      "useColumnNames": true
    },

    /**
     * data loader for events data
     */
    "eventDataLoader": {
      "url": "https://www.amcharts.com/wp-content/uploads/assets/stock/MSFT_events.csv",
      "format": "csv",
      "showCurtain": true,
      "showErrors": true,
      "async": true,
      "reverse": true,
      "delimiter": ",",
      "useColumnNames": true,
      "postProcess": function( data ) {
        for ( var x in data ) {
          switch ( data[ x ].Type ) {
            case 'A':
              var color = "#f9d423";
              break;
            default:
              var color = "#0fd850";
              break;
          }
          data[ x ].Description = data[ x ].Description.replace( "Upgrade", "<strong style=\"color: #0c0\">Upgrade</strong>" ).replace( "Downgrade", "<strong style=\"color: #c00\">Downgrade</strong>" );
          data[ x ] = {
            "type": "pin",
            "graph": "g1",
            "backgroundColor": color,
            "date": data[ x ].Date,
            "text": data[ x ].Type,
            "description": "<strong>" + data[ x ].Title + "</strong><br />" + data[ x ].Description
          };
        }
        return data;
      }
    }

  }, {
    "title": "TXN",
    "fieldMappings": [ {
      "fromField": "Open",
      "toField": "open"
    }, {
      "fromField": "High",
      "toField": "high"
    }, {
      "fromField": "Low",
      "toField": "low"
    }, {
      "fromField": "Close",
      "toField": "close"
    }, {
      "fromField": "Volume",
      "toField": "volume"
    } ],
    "compared": true,
    "categoryField": "Date",
    "dataLoader": {
      "url": "https://www.amcharts.com/wp-content/uploads/assets/stock/TXN.csv",
      "format": "csv",
      "showCurtain": true,
      "showErrors": true,
      "async": true,
      "reverse": true,
      "delimiter": ",",
      "useColumnNames": true
    }
  } ],
  "dataDateFormat": "YYYY-MM-DD",

  "panels": [ {
      "title": "Value",
      "percentHeight": 50,

      "stockGraphs": [ {
        "type": "candlestick",
        "id": "g1",
        "openField": "open",
        "closeField": "close",
        "highField": "high",
        "lowField": "low",
        "valueField": "close",
        "lineColor": "#fff",
        "fillColors": "#fff",
        "negativeLineColor": "#cc208e",
        "negativeFillColors": ["#cc208e", "#6713d2"],
        "fillAlphas": 1,
        "comparedGraphLineThickness": 2,
        "columnWidth": 0.5,
        "useDataSetColors": false,
        "comparable": true,
        "compareField": "close",
        "showBalloon": false,
        "proCandlesticks": true
      } ],

      "stockLegend": {
        "valueTextRegular": undefined,
        "periodValueTextComparing": "[[percents.value.close]]%"
      }

    },

    {
      "title": "Volume",
      "percentHeight": 30,
      "marginTop": 1,
      "columnWidth": 0.4,
      "showCategoryAxis": false,

      "stockGraphs": [ {
        "valueField": "volume",
        "openField": "open",
        "type": "column",
        "showBalloon": false,
        "fillAlphas": 1,
        "lineColor": ["rgba(149,20,255,1)", "rgba(225,5,219,1)", "#2575fc"],
        "fillColors": ["rgba(149,20,255,1)", "rgba(225,5,219,1)", "#2575fc"],
        "negativeLineColor": "#cc208e",
        "negativeFillColors": ["#cc208e", "#6713d2"],
        "useDataSetColors": false
      } ],

      "stockLegend": {
        "markerType": "none",
        "markerSize": 0,
        "labelText": "",
        "periodValueTextRegular": "[[value.close]]"
      },

      "valueAxes": [ {
        "usePrefixes": true
      } ]
    }
  ],

  "panelsSettings": {
    //    "color": "#fff",
    "plotAreaFillColors": "#130b3e",
    "plotAreaFillAlphas": 1,
    "marginLeft": 0,
    "marginTop": 5,
    "marginBottom": 5
  },

  "chartScrollbarSettings": {
    "graph": "g1",
    "graphType": "line",
    "usePeriod": "WW",
    "backgroundColor": "#130b3e",
    "graphFillColor": "#130b3e",
    "graphFillAlpha": 0.5,
    "gridColor": "#130b3e",
    "gridAlpha": 1,
    "selectedBackgroundColor": "#130b3e",
    "selectedGraphFillAlpha": 1
  },

  "categoryAxesSettings": {
    "equalSpacing": true,
    "gridColor": "#130b3e",
    "gridAlpha": 1
  },

  "valueAxesSettings": {
    "gridColor": "#130b3e",
    "gridAlpha": 1,
    "inside": false,
    "showLastLabel": true
  },

  "chartCursorSettings": {
    "pan": true,
    "valueLineEnabled": true,
    "valueLineBalloonEnabled": true
  },

  "legendSettings": {
    //"color": "#fff"
  },

  "stockEventsSettings": {
    "showAt": "high",
    "type": "pin"
  },

  "balloon": {
    "textAlign": "left",
    "offsetY": 10
  },

  "periodSelector": {
    "position": "bottom",
    "periods": [ {
        "period": "DD",
        "count": 10,
        "label": "10D"
      }, {
        "period": "MM",
        "count": 1,
        "label": "1M"
      }, {
        "period": "MM",
        "count": 6,
        "label": "6M"
      }, {
        "period": "YYYY",
        "count": 1,
        "label": "1Y"
      }, {
        "period": "YYYY",
        "count": 2,
        "selected": true,
        "label": "2Y"
      },
      /* {
           "period": "YTD",
           "label": "YTD"
         },*/
      {
        "period": "MAX",
        "label": "MAX"
      }
    ]
  }
} );



//=------------------------chartdiv30


var chartData = generateChartData();

function generateChartData() {
  var chartData = [];
  var firstDate = new Date( 2012, 0, 1 );
  firstDate.setDate( firstDate.getDate() - 1000 );
  firstDate.setHours( 0, 0, 0, 0 );

  var a = 2000;
 
  for ( var i = 0; i < 1000; i++ ) {
    var newDate = new Date( firstDate );
    newDate.setHours( 0, i, 0, 0 );

    a += Math.round((Math.random()<0.5?1:-1)*Math.random()*10);
    var b = Math.round( Math.random() * 100000000 );

    chartData.push( {
      "date": newDate,
      "value": a,
      "volume": b
    } );
  }
  return chartData;
}

var chart = AmCharts.makeChart( "chartdiv30", {
  "type": "stock",
  "theme": "dark",
  "categoryAxesSettings": {
    "minPeriod": "mm"
  },

  "dataSets": [ {
    "color": ["#fc6076", "#ff9a44"],
    "fieldMappings": [ {
      "fromField": "value",
      "toField": "value"
    }, {
      "fromField": "volume",
      "toField": "volume"
    } ],

    "dataProvider": chartData,
    "categoryField": "date"
  } ],

  "panels": [ {
    "showCategoryAxis": false,
    "title": "Value",
    "percentHeight": 70,

    "stockGraphs": [ {
      "id": "g1",
      "valueField": "value",
      "type": "smoothedLine",
      "lineThickness": 2,
      "bullet": "round"
    } ],


    "stockLegend": {
      "valueTextRegular": " ",
      "markerType": "none"
    }
  }, {
    "title": "Volume",
    "percentHeight": 50,
    "stockGraphs": [ {
      "valueField": "volume",
      "type": "column",
      "cornerRadiusTop": 2,
      "fillAlphas": 1
    } ],

    "stockLegend": {
      "valueTextRegular": " ",
      "markerType": "none"
    }
  } ],

  "chartScrollbarSettings": {
    "graph": "g1",
    "usePeriod": "10mm",
    "position": "top"
  },

  "chartCursorSettings": {
    "valueBalloonsEnabled": true
  },

  "periodSelector": {
    "position": "top",
    "dateFormat": "YYYY-MM-DD JJ:NN",
    "inputFieldWidth": 80,
    "periods": [ {
      "period": "hh",
      "count": 1,
      "label": "1 hour"
    }, {
      "period": "hh",
      "count": 2,
      "label": "2 hours"
    }, {
      "period": "hh",
      "count": 5,
      "selected": true,
      "label": "5 hour"
    }, {
      "period": "hh",
      "count": 12,
      "label": "12 hours"
    }, {
      "period": "MAX",
      "label": "MAX"
    } ]
  },

  "panelsSettings": {
    "usePrefixes": true
  },

  "export": {
    "enabled": true,
    "position": "bottom-right"
  }
} );


//=------------------------chartdiv22

var chart = AmCharts.makeChart("chartdiv22", {
  "type": "serial",
  "theme": "dark",
  "dataDateFormat": "YYYY-MM-DD",
  "precision": 2,
  "valueAxes": [{
    "id": "v1",
    "title": "Sales",
    "position": "left",
    "autoGridCount": false,
    "labelFunction": function(value) {
      return "$" + Math.round(value) + "M";
    }
  }, {
    "id": "v2",
    "title": "Market Days",
    "gridAlpha": 0,
    "position": "right",
    "autoGridCount": false
  }],
  "graphs": [{
    "id": "g3",
    "valueAxis": "v1",
    "lineColor": "#0fd850",
    "fillColors": ["#fc6076", "#ff9a44"],
    "fillAlphas": 1,
    "type": "column",
    "title": "Actual Sales",
    "valueField": "sales2",
    "clustered": false,
    "columnWidth": 0.5,
    "legendValueText": "$[[value]]M",
    "balloonText": "[[title]]<br /><b style='font-size: 130%'>$[[value]]M</b>"
  }, {
    "id": "g4",
    "valueAxis": "v1",
    "lineColor": "#cc208e",
    "fillColors": ["#cc208e", "#6713d2"],
    "fillAlphas": 1,
    "type": "column",
    "title": "Target Sales",
    "valueField": "sales1",
    "clustered": false,
    "columnWidth": 0.3,
    "legendValueText": "$[[value]]M",
    "balloonText": "[[title]]<br /><b style='font-size: 130%'>$[[value]]M</b>"
  }, {
    "id": "g1",
    "valueAxis": "v2",
    "bullet": "round",
    "bulletBorderAlpha": 1,
    "bulletColor": "#FFFFFF",
    "bulletSize": 5,
    "hideBulletsCount": 50,
    "lineThickness": 2,
    "lineColor": "#6713d2",
    "type": "smoothedLine",
    "title": "Market Days",
    "useLineColorForBulletBorder": true,
    "valueField": "market1",
    "balloonText": "[[title]]<br /><b style='font-size: 130%'>[[value]]</b>"
  }, {
    "id": "g2",
    "valueAxis": "v2",
    "bullet": "round",
    "bulletBorderAlpha": 1,
    "bulletColor": "#FFFFFF",
    "bulletSize": 5,
    "hideBulletsCount": 50,
    "lineThickness": 2,
    "lineColor": "#e1ede9",
    "type": "smoothedLine",
    "dashLength": 5,
    "title": "Market Days ALL",
    "useLineColorForBulletBorder": true,
    "valueField": "market2",
    "balloonText": "[[title]]<br /><b style='font-size: 130%'>[[value]]</b>"
  }],
  "chartScrollbar": {
    "graph": "g1",
    "oppositeAxis": false,
    "offset": 30,
    "scrollbarHeight": 50,
    "backgroundAlpha": 0,
    "selectedBackgroundAlpha": 0.1,
    "selectedBackgroundColor": "#888888",
    "graphFillAlpha": 0,
    "graphLineAlpha": 0.5,
    "selectedGraphFillAlpha": 0,
    "selectedGraphLineAlpha": 1,
    "autoGridCount": true,
    "color": "#AAAAAA"
  },
  "chartCursor": {
    "pan": true,
    "valueLineEnabled": true,
    "valueLineBalloonEnabled": true,
    "cursorAlpha": 0,
    "valueLineAlpha": 0.2
  },
  "categoryField": "date",
  "categoryAxis": {
    "parseDates": true,
    "dashLength": 1,
    "minorGridEnabled": true
  },
  "legend": {
    "useGraphSettings": true,
    "position": "top"
  },
  "balloon": {
    "borderThickness": 1,
    "shadowAlpha": 0
  },
  "export": {
   "enabled": true
  },
  "dataProvider": [{
    "date": "2013-01-16",
    "market1": 71,
    "market2": 75,
    "sales1": 5,
    "sales2": 8
  }, {
    "date": "2013-01-17",
    "market1": 74,
    "market2": 78,
    "sales1": 4,
    "sales2": 6
  }, {
    "date": "2013-01-18",
    "market1": 78,
    "market2": 88,
    "sales1": 5,
    "sales2": 2
  }, {
    "date": "2013-01-19",
    "market1": 85,
    "market2": 89,
    "sales1": 8,
    "sales2": 9
  }, {
    "date": "2013-01-20",
    "market1": 82,
    "market2": 89,
    "sales1": 9,
    "sales2": 6
  }, {
    "date": "2013-01-21",
    "market1": 83,
    "market2": 85,
    "sales1": 3,
    "sales2": 5
  }, {
    "date": "2013-01-22",
    "market1": 88,
    "market2": 92,
    "sales1": 5,
    "sales2": 7
  }, {
    "date": "2013-01-23",
    "market1": 85,
    "market2": 90,
    "sales1": 7,
    "sales2": 6
  }, {
    "date": "2013-01-24",
    "market1": 85,
    "market2": 91,
    "sales1": 9,
    "sales2": 5
  }, {
    "date": "2013-01-25",
    "market1": 80,
    "market2": 84,
    "sales1": 5,
    "sales2": 8
  }, {
    "date": "2013-01-26",
    "market1": 87,
    "market2": 92,
    "sales1": 4,
    "sales2": 8
  }, {
    "date": "2013-01-27",
    "market1": 84,
    "market2": 87,
    "sales1": 3,
    "sales2": 4
  }, {
    "date": "2013-01-28",
    "market1": 83,
    "market2": 88,
    "sales1": 5,
    "sales2": 7
  }, {
    "date": "2013-01-29",
    "market1": 84,
    "market2": 87,
    "sales1": 5,
    "sales2": 8
  }, {
    "date": "2013-01-30",
    "market1": 81,
    "market2": 85,
    "sales1": 4,
    "sales2": 7
  }]
});



//---echart2
var dom = document.getElementById("e_chart_2");
var myChart = echarts.init(dom);
var app = {};
option = null;
option = {
	color: ["#fc6076", "#ff9a44"],
	textStyle: {
		color: '#fff'
	},
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['the highest temperature','the lowest temperature']
    },
	
    xAxis:  {
        type: 'category',
        boundaryGap: false,
        data: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    },
    yAxis: {
        type: 'value',
        axisLabel: {
            formatter: '{value}'
        }
    },
    series: [
        {
            name:'Maximum',
            type:'line',
            data:[220, 182, 191, 234, 190, 330, 310],
            markPoint: {
                data: [
                    {type: 'max', name: 'Maximum'},
                    {type: 'min', name: 'Minimum'}
                ]
            },
            markLine: {
                data: [
                    {type: 'average', name: 'Average'}
                ]
            }
        }
    ]
};
if (option && typeof option === "object") {
    myChart.setOption(option, true);
}


//=-------------------------chartdiv31

var chart = AmCharts.makeChart( "chartdiv31", {
  "theme": "dark",
  "type": "gauge",
  "axes": [ {
    "axisColor": "#6713d2",
    "axisThickness": 3,
    "endValue": 240,
    "gridInside": false,
    "inside": false,
    "radius": "100%",
    "valueInterval": 20,
    "tickColor": "#6713d2"
  }, {
    "axisColor": "#cc208e",
    "axisThickness": 3,
    "endValue": 160,
    "radius": "80%",
    "valueInterval": 20,
    "tickColor": "#cc208e"
  } ],
  "arrows": [ {
    "color": "#6713d2",
    "innerRadius": "10%",
    "nailRadius": 0,
    "radius": "75%"
  } ],
  "export": {
    "enabled": true
  }
} );

setInterval( randomValue, 2000 );

// set random value
function randomValue() {
  var value = Math.round( Math.random() * 240 );
  chart.arrows[ 0 ].setValue( value );
}



    /*
     * Flot Interactive Chart
     * -----------------------
     */
    // We use an inline data source in the example, usually data would
    // be fetched from a server
    var data = [], totalPoints = 200

    function getRandomData() {

      if (data.length > 0)
        data = data.slice(1)

      // Do a random walk
      while (data.length < totalPoints) {

        var prev = data.length > 0 ? data[data.length - 1] : 50,
            y    = prev + Math.random() * 10 - 5

        if (y < 0) {
          y = 0
        } else if (y > 100) {
          y = 100
        }

        data.push(y)
      }

      // Zip the generated y values with the x values
      var res = []
      for (var i = 0; i < data.length; ++i) {
        res.push([i, data[i]])
      }

      return res
    }

    var interactive_plot = $.plot('#interactive', [getRandomData()], {
      grid: {
            color: "#AFAFAF"
            , hoverable: true
            , borderWidth: 0
            , backgroundColor: '#130b3e'
        },
      series: {
        shadowSize: 0, // Drawing is faster without shadows
        color     : '#6713d2'
      },
	  tooltip: true,
      lines : {
        fill : '#6713d2', //Converts the line chart to area chart
        color: '#6713d2'
      },
	  tooltipOpts: {
            content: "Visit: %y"
            , defaultTheme: false
        },
      yaxis : {
        min : 0,
        max : 100,
        show: true
      },
      xaxis : {
        show: true
      }
    })

    var updateInterval = 50 //Fetch data ever x milliseconds
    var realtime       = 'on' //If == to on then fetch data every x seconds. else stop fetching
    function update() {

      interactive_plot.setData([getRandomData()])

      // Since the axes don't change, we don't need to call plot.setupGrid()
      interactive_plot.draw()
      if (realtime === 'on')
        setTimeout(update, updateInterval)
    }

    //INITIALIZE REALTIME DATA FETCHING
    if (realtime === 'on') {
      update()
    }
    
    /*
     * END INTERACTIVE CHART
     */
