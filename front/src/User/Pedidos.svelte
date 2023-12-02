<script>
    import { link, push } from 'svelte-spa-router';
	import { onMount } from 'svelte';
	import { isAuthenticated } from '../js/auth';
	import axios from 'axios';

    import NavUser from "../Components/NavUser.svelte";

	let datos = [];

	const getOrders = async () => {
		const url = 'http://34.70.30.227:5000/orders/identity_id/' + localStorage.getItem('id');
		//const response = await axios.get(`http://34.70.30.227:5000/orders/identity_id/${localStorage.getItem('id')}`);		
		const response = await axios.get(url);		
		console.log(response.data.data)	
		return response.data.data;
	}

	onMount(() => {
		if (!isAuthenticated() || localStorage.getItem('admin') != '0'){
			push('/');


		}

		const data = getOrders();

		datos = data;

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
							{#each datos as dato}
								<td> {dato.id }</td>
								<td>

									<a href="/detalles/pedido/{dato.id}" use:link ><button class="crud-detalles mx-2 btn btn-outline-info" value="">{dato.status}</button></a>

								</td>
							{/each}	
						</tr>
				</tbody>
			</table>
		</div>
	</div>