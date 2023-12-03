<script>
    import { onMount } from 'svelte';
    import { isAuthenticated } from '../js/auth';
    import { push } from 'svelte-spa-router';
    import { getFunction } from '../js/asyncFunctions';
    import NavAdmin from '../Components/NavAdmin.svelte';
    import Highcharts from 'highcharts';
    import HighchartsExporting from 'highcharts/modules/exporting';
  
    let rutas = [];
    let distancia = [];
    let chart1;
    let chart2;
  
    HighchartsExporting(Highcharts);
  
    onMount(async () => {
		if (!isAuthenticated() || localStorage.getItem('admin') !== '1') {
			push('/');
		}
	
		rutas = await getFunction('http://34.70.30.227:5000/graph1');
		distancia = await getFunction('http://34.70.30.227:5000/graph2');

		chart1 = Highcharts.chart('rutas', {
			chart: {
				type: 'column'
			},
			title: {
				text: 'Distancia promedio por compañia'
			},
			series: [{
				name:'ID Compañia',
				data: rutas
			}]
		});

		chart2 = Highcharts.chart('distancia', {
			chart: {
				type: 'column'
			},
			title: {
				text: 'Cantidad de rutas por compañia'
			},
			series: [{
				name:'ID Compañia',
				data: distancia
			}]
		});
    });
</script>
  
<NavAdmin />
  
<div class="container mt-5 bg-white rounded shadow pt-5 pb-5 p-5 h-100 mb-5 w-100">
    <div class="container">
        <h1 class="text-center mb-5"> Estadisticas de la compañia </h1>
    </div>

    <div class="row ">

        <div class="col">
            <div id="rutas"></div>
        </div>

        <div class="col">
            <div id="distancia"></div>
        </div>

    </div>
</div>
  