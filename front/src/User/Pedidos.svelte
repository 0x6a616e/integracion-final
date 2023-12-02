<script>
    import { link, push } from 'svelte-spa-router';
	import { onMount } from 'svelte';
	import { isAuthenticated } from '../js/auth';
	import {getFunction} from '../js/asyncFunctions';
    import NavUser from "../Components/NavUser.svelte";

	let datos = [];
	
	onMount( async () => {
		if (!isAuthenticated() || localStorage.getItem('admin') != '0'){
			push('/');


		}

		datos = await getFunction('http://34.70.30.227:5000/orders/identity_id/' + localStorage.getItem('id'));

	});



</script>

<NavUser />

<div class="container mt-5 bg-white rounded shadow pt-5 pb-5 p-5 h-100 mb-5 w-100">
		<div class="container">
			<h1 class="text-center mb-5">Pedidos Realizados </h1>
		</div>
		<div class="container mt-5">
			<table class="table" style="table-layout: fixed ; width: 100% ;">
				<thead class="table-dark">
					<tr>
                        
                        <th scope="col">#</th>
                        <th scope="col">Acciones</th>
					</tr>
				</thead>

				<tbody class="w-100">
					{#each datos as dato}
						<tr>
							<td> {dato.id }</td>
							<td>
								<a href="/detalles/pedido/{dato.id}" use:link ><button class="crud-detalles mx-2 btn btn-outline-info" value="">Detalles</button></a>
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	</div>