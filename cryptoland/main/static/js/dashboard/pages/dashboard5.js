//[Dashboard Javascript]

//Project:	Crypto Admin - Responsive Admin Template
//Primary use:   Used only for the main dashboard (index.html)


$(function () {

  'use strict';
	
		
//ticker
 	if ($('#webticker-1').length) {   
		$("#webticker-1").webTicker({
			height:'auto', 
			duplicate:true, 
			startEmpty:false, 
			rssfrequency:5
		});
	}
	
	/*--- Sparkline charts - mini charts ---*/ 
		function sparkline_charts() {
			$('.sparklines').sparkline('html');
		}
		if ($('.sparklines').length) {
			sparkline_charts();
		} 

	
	
}); // End of use strict




                


