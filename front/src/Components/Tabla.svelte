<script>
	import { link } from "svelte-spa-router";
	import {deleteData} from "../js/asyncFunctions";
    export let tipo = "";
    export let objetos = [""];
	export let url = "";
	export let tabla = "";
</script>


<div class="container mt-5 bg-white rounded shadow pt-5 pb-5 p-5 h-100 mb-5 w-100">
		<div class="container">
			<h1 class="text-center mb-5">{tipo}</h1>
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
					{#each objetos as objeto}
						<tr>
							<td> {objeto.id} </td>
							<td> {objeto.name} </td>
							<td>

								<a href="/detalles/{url}/admin/{objeto.id}" use:link ><button class="crud-detalles mx-2 btn btn-outline-info" value="">Detalles</button></a>
								<a href="/editar/{url}/admin/{objeto.id}" use:link ><button class="crud-editar btn btn-outline-primary" value="">Editar</button></a>
								<button on:click={() => deleteData(`http://34.70.30.227:5000/data/${tabla}/${objeto.id}`)} class="crud-eliminar mx-2 btn btn-outline-danger" value="">Eliminar</button>

							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	</div>