<script>
    import NavAdmin from '../Components/NavAdmin.svelte';
</script>

<NavAdmin />

<div class="container mt-5 bg-white rounded shadow pt-5 pb-5 p-5 h-100 mb-5 w-100">
		<div class="container">
			<h1 class="text-center mb-5">Sucursales</h1>
		</div>
		<div class="container mt-5">
			<table class="table" style="table-layout: fixed ; width: 100% ;">
				<thead class="table-dark">
					<tr>
					<th scope="col">#</th>
					<th scope="col">Nombre</th>
					<th scope="col">Acciones</th>
					</tr>
				</thead>
				<tbody class="w-100">
                    <tr>
                        <td> 1 </td>
                        <td> Sucursal 1 </td>
                        <td>

                            <button class="crud-detalles mx-2 btn btn-outline-info" value="">Detalles</button>
                            <button class="crud-editar btn btn-outline-primary" value="">Editar</button>
                            <button data-type="branch" class="crud-eliminar mx-2 btn btn-outline-danger" value="">Eliminar</button>

                        </td>
                    </tr>
				</tbody>
			</table>
		</div>
	</div>