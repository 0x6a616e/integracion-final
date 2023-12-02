<script>
    import { onMount } from 'svelte';
	import { isAuthenticated } from '../../js/auth';
    import { push } from 'svelte-spa-router';
    import NavAdmin from '../../Components/NavAdmin.svelte';

    onMount(() => {
		if (!isAuthenticated() || localStorage.getItem('admin') != '1' ){
			push('/');
		}
	});

</script>

<NavAdmin />

<div class="container mt-5 bg-white rounded shadow pt-5 pb-5 p-5 h-100 mb-5 w-100">
    <div class="container">
        <h1 class="text-center mb-5"> Asignar  Orden </h1>
    </div>

    <form action="/orders/asign/payment" method="POST">
        
        <div class="col">
            <div class="branches my-3">

                <label for="branch" class="form-label">Seleccione una Sucursal </label>
                
                <select id="branches" class="form-select" name="branch" aria-label="Default select example">
                    <option selected> -- Selecciona un Sucursal -- </option>
                    <option value=""> Sucursal 1 </option>
                </select>
            </div>
            
            <div class="company my-3">
                
                <label for="company" class="form-label">Seleccione una compañia </label>
                
                <select id="company" class="form-select" name="company" aria-label="Default select example">
                    <option selected> -- Selecciona un Compañia -- </option>
                
                    </select>

            </div>
            
            <div class="vehicle my-3">
                
                <label for="vehicle" class="form-label">Seleccione un vehiculo </label>
                
                <select id="vehicle" class="form-select" name="vehicle" aria-label="Default select example">
                    <option selected> -- Selecciona un Vehiculo -- </option>
                </select>
            </div>
        </div>
        <div class="my-5 justiy-content-center">
            <button type="submit" class="btn center w-100 btn-lg btn-block shadow-lg text-light" style=" background-color: #8973D9">Asignar</button>
        </div>
    </form>
</div>
