<script>
    import { onMount } from 'svelte';
	import { isAuthenticated } from '../js/auth';
    import { link, push } from 'svelte-spa-router';
    import { getFunction, deleteData} from '../js/asyncFunctions';
    import NavAdmin from '../Components/NavAdmin.svelte';

    let ordenes = [];
    onMount(async () => {
		if (!isAuthenticated() || localStorage.getItem('admin') != '1'){
			push('/');
		}

        ordenes = await getFunction('http://34.70.30.227:5000/data/orders');

	});

</script>

<NavAdmin />

<div class="container mt-5 bg-white rounded shadow pt-5 pb-5 p-5 h-100 mb-5 w-100">
    <div class="container">
        <h1 class="text-center mb-5"> Ordenes </h1>
    </div>
    <div class="container">
        <div class="d-flex">
            <a href="/nuevopedido/admin" use:link><button class="btn btn-outline-success">Crear Nueva Orden </button></a>
        </div>
    </div> 
    
    <div class="container mt-5">
    <table class="table" style="table-layout: fixed ; width: 100% ;">
        <thead class="table-dark">
            <tr>
            <th scope="col">#</th>
            <th scope="col">Estatus</th>
            <th scope="col">Acciones</th>
            </tr>
        </thead>

        <tbody class="w-100">
            {#each ordenes as orden}
                <tr>
                    <td class="t1"> {orden.id} </td>
                    <td class="t1"> {orden.status} </td>
                    <td class="t2">
                        <div class="container row">
                            <div class="col">
                                    <a href="/asignar/camion/admin/{orden.id}" use:link><button class="asign w-100 my-2 btn btn-outline-success" value="">Asignacion</button></a>
                                    <a href="/detalles/pedido/admin/{orden.id}" use:link ><button class="w-100 my-2 crud-detalles btn btn-outline-info" value="">Detalles</button></a>
                            </div>
                            <div class="col">
                                <button on:click={() => deleteData(`http://34.70.30.227:5000/data/orders/${orden.id}`)} class="w-100 my-2 crud-eliminar btn btn-outline-danger" value="">Eliminar</button>
                            </div>
                        </div>
                    </td>
                </tr>
            {/each}
        </tbody>
        </table>
    </div>

</div>