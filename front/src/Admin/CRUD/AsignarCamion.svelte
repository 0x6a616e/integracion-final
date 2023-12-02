<script>
    import { onMount } from 'svelte';
	import { isAuthenticated } from '../../js/auth';
    import { push } from 'svelte-spa-router';
    import {getFunction, patchForm} from '../../js/asyncFunctions';
    import NavAdmin from '../../Components/NavAdmin.svelte';

    export let params = {};
    
    let sucursales = [];

    let compañias = [];

    let camiones = [];

    onMount(async () => {
		if (!isAuthenticated() || localStorage.getItem('admin') != '1' ){
			push('/');
		}

        sucursales = await getFunction('http://34.70.30.227:5000/data/branch');

        compañias = await getFunction('http://34.70.30.227:5000/data/company');

        camiones = await getFunction('http://34.70.30.227:5000/data/truck');
	});

</script>

<NavAdmin />

<div class="container mt-5 bg-white rounded shadow pt-5 pb-5 p-5 h-100 mb-5 w-100">
    <div class="container">
        <h1 class="text-center mb-5"> Asignar  Orden </h1>
    </div>

    <form  on:submit|preventDefault={() => patchForm(`http://34.70.30.227:5000/order/${params.id}`)} id="form-product">
        
        <div class="col">
            <div class="branches my-3">

                <label for="branch" class="form-label">Seleccione una Sucursal </label>
                
                <select id="branches" class="form-select" name="branch" aria-label="Default select example">
                    <option selected> -- Selecciona un Sucursal -- </option>
                    {#each sucursales as sucursal}
                        <option value="{sucursal.id}"> {sucursal.name} </option>
                    {/each}
                </select>
            </div>
            
            <div class="company my-3">
                
                <label for="company" class="form-label">Seleccione una compañia </label>
                
                <select id="company" class="form-select" name="company" aria-label="Default select example">
                    <option selected> -- Selecciona un Compañia -- </option>
                
                    {#each compañias as compañia}
                        <option value="{compañia.id}"> {compañia.name} </option>
                    {/each}
                </select>

            </div>
            
            <div class="vehicle my-3">
                
                <label for="truck" class="form-label">Seleccione un vehiculo </label>
                
                <select id="vehicle" class="form-select" name="truck" aria-label="Default select example">
                    <option selected> -- Selecciona un Vehiculo -- </option>


                    {#each camiones as camion}
                        <option value="{camion.id}"> {camion.name} </option>
                    {/each}

                </select>
            </div>
        </div>
        <div class="my-5 justiy-content-center">
            <button type="submit" class="btn center w-100 btn-lg btn-block shadow-lg text-light" style=" background-color: #8973D9">Asignar</button>
        </div>
    </form>
</div>
