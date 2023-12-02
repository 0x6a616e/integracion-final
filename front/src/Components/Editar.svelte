<script>
    import {patchForm} from '../js/asyncFunctions';
    export let label = "";
    export let id = "";
    export let attrs = [];
    export let table = "";
</script>

<div class="container mt-5 bg-white rounded shadow pt-5 pb-5 p-5 h-100 mb-5 w-100">
    <div class="container">
        <h1 class="text-center mb-5"> Editar { label } </h1>
    </div>
    <div class="container my-5">

        <h5>ID { label } : { id } </h5>
    </div>

    <form on:submit|preventDefault={() => patchForm(`http://34.70.30.227:5000/data/${table}/${id}`)} id="form-product">

        <div class="row">
            <div class="col">
                <label for="atributo" class="form-label"> Atributo </label>
                <select class="form-select" name="atributo" aria-label="Default select example">
                    <option selected> -- Selecciona un Atributo -- </option>
                    {#each attrs as  attr }
                        <option value="{attr}"> {attr} </option>
                    {/each}
                </select>
            </div>
            <div class="col">
                <label for="valor" class="form-label">Valor nuevo </label>
                <input type="text" class="form-control" name="valor">
            </div>
        </div>
        <div class="my-5 justiy-content-center">
            <button type="submit" class="btn center w-100 btn-lg btn-block shadow-lg text-light" style=" background-color: #8973D9">Realizar cambio</button>
        </div>
    </form>
</div>
