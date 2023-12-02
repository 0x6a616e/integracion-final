<script>
    import { onMount } from 'svelte';
	import { isAuthenticated } from '../js/auth';
    import { push } from 'svelte-spa-router';
    import NavAdmin from '../Components/NavAdmin.svelte';

    onMount(async () => {
		if (!isAuthenticated() || localStorage.getItem('admin') != '1'){
			push('/');
		}

	});

</script>

<NavAdmin />

<div class="container mt-5 bg-white rounded shadow pt-5 pb-5 p-5 h-100 mb-5 w-100">
    <div class="container">
        <h1 class="text-center mb-5"> Estadisticas de la compañia </h1>
    </div>

    <div class="row ">
        <div class="col" style="margin-left: 10rem;">
            <img style="width: 80%;" src="http://34.170.178.166/~j18366496/mean_distance_per_company.png" alt="Distancia promedio">
        </div>
        <div class="col">
            <img  style="width: 80%;"src="http://34.170.178.166/~j18366496/routes_per_company.png" alt="Cantidad de rutas por compañia">
        </div>
    </div>

</div>