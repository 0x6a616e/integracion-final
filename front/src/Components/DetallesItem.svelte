<script>
    export let tipo = "";
    export let tables = [];
</script>

<div class="container mt-5 bg-white rounded shadow pt-5 pb-5 p-5 h-100 mb-5 w-100">
    <div class="container">
        <h2 class="text-center mb-5"> Detalles de { tipo } </h2>
    </div>
    <div class="container my-5">
        <table class="table table-striped-columns">
            <thead>
                <th> Atributo </th>
                <th> Valor </th>
            </thead>
            <tbody>
                {#each tables as table }
                    <tr>
                        <td> {table[0]} </td>
                        <td> {table[1][1]} </td>
                    </tr>
                {/each}
            </tbody>
        </table>

    </div>
</div>