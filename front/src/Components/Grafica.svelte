<script>
    import { onMount } from 'svelte';
    import Highcharts from 'highcharts';
    import HighchartsExporting from 'highcharts/modules/exporting';
    
    export let id = "";
    export let titulo = "";
    export let data = [];

    
    HighchartsExporting(Highcharts);

    let chart; 

    onMount(() => {
        console.log(data);
        chart = Highcharts.chart(id, 
            {
                chart: {
                    type: 'column'
                },
                title: {
                    text: titulo
                },
                series: [{
                    data: data 
                }]
            }
        );
    });

</script>

<div id={id}></div>

<style>
  #miGrafico {
    width: 100%;
    height: 400px;
  }
</style>
