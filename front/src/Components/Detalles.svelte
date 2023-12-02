<script>

    import Map from "./Map.svelte";

    export let x = 0;
    export let y = 0;
    export let items = [];

</script>


<div class="container mt-4 bg-white rounded shadow pt-5 pb-5 p-5 h-100 mb-5">
    <div class="container"> 

        <center>
            <h1> Detalles del pedido </h1>
        </center>

    </div>
    <div class="row mt-5">
        <div class="col">

            <Map x = {x} y = {y} />

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
                    {#each items as item}
						<tr>
						    <td> {item.name}  </td>
							<td> {item.quantity}</td>
						</tr>
                    {/each}
				</tbody>
			</table>
        </div>

    </div>
</div>