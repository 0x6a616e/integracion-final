<script>
    import { link, push } from 'svelte-spa-router';
	import { onMount } from 'svelte';
	import { isAuthenticated } from '../js/auth';
    import NavUser from "../Components/NavUser.svelte";

	onMount(() => {
		if (!isAuthenticated()){
			push('/');
		}
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
						<tr>
							<td> 1 </td>
							<td>
								<a href="/detalles/pedido/1" use:link ><button class="crud-detalles mx-2 btn btn-outline-info" value="">Detalles</button></a>

							</td>
						</tr>
				</tbody>
			</table>
		</div>
	</div>