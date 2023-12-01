<script>
    import { link } from 'svelte-spa-router';
    import NavAdmin from '../Components/NavAdmin.svelte';
</script>

<NavAdmin />

<div class="container mt-5 bg-white rounded shadow pt-5 pb-5 p-5 h-100 mb-5 w-100">
    <div class="container">
        <h1 class="text-center mb-5"> Ordenes </h1>
    </div>
    <div class="container">
        <div class="d-flex">
            <a href="/nuevopedidoadmin" use:link><button class="btn btn-outline-success">Crear Nueva Orden </button></a>
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
                <tr>
                    <td class="t1"> 1 </td>
                    <td class="t1"> Orden 1 </td>
                    <td class="t2">
                        <div class="container row">
                            <div class="col">
                                    <button class="asign w-100 my-2 btn btn-outline-success" value="">Asignacion</button>
                                    <button class="w-100 my-2 crud-detalles btn btn-outline-info" value="">Detalles</button>
                            </div>
                            <div class="col">
                                <button data-type="order" class="w-100 my-2 crud-eliminar btn btn-outline-danger" value="">Eliminar</button>
                            </div>
                        </div>
                    </td>
                </tr>
        </tbody>
        </table>
    </div>

</div>