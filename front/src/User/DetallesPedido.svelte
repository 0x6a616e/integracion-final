<script>

    import NavUser from "../Components/NavUser.svelte";
    import Map from "../Components/Map.svelte";
</script>

<NavUser />

<div class="container mt-4 bg-white rounded shadow pt-5 pb-5 p-5 h-100 mb-5">
    <div class="container"> 

        <center>
            <h1> Detalles del pedido </h1>
        </center>

    </div>
    <div class="row mt-5">
        <div class="col">

            <Map />

        </div>

        <div class="col">
            <table class="table" style="table-layout: fixed ; width: 100% ;">
				<thead class="table-dark">
					<tr>
                        
                        <th scope="col">Item</th>
                        <th scope="col">Cantidad </th>
					</tr>
				</thead>

				<tbody class="w-100">
						<tr>
						    <td> 22 kilates  </td>
							<td>
                                2
							</td>
						</tr>
				</tbody>
			</table>
        </div>

    </div>
</div>
