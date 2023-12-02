<script>

    import { onMount } from "svelte";
    import { isAuthenticated } from '../../js/auth';
    import { push } from 'svelte-spa-router';
    import {getFunction} from '../../js/asyncFunctions';
    import axios from "axios";
    import NavAdmin from "../../Components/NavAdmin.svelte";

    let users = [];

    const submitForm = async () => {
        const form = document.getElementById('form-product');
        const headers = {headers : {'Authorization' : `Bearer ${localStorage.getItem('token')}`} }  
        await axios.post('http://34.70.30.227:5000/order', form, headers );
    }

    onMount( async () => {

        if (!isAuthenticated() || localStorage.getItem('admin') != '1'){
			push('/');
		}

        users = await getFunction('http://34.70.30.227:5000/data/identity');

        const handleClick = async () => {
            try {
                const response = await axios.get('http://34.70.30.227:5000/data/products');
                const data = response.data.data;

                const dropdown = document.createElement("select");
                dropdown.classList.add("form-select", "w-50", "mt-2");
                dropdown.setAttribute('name', 'modelo');

                data.forEach(objeto => {
                    const opcion = document.createElement("option");
                    opcion.text = objeto.id + " | " + objeto.description;
                    opcion.setAttribute("value", objeto.id)
                    dropdown.add(opcion);
                });

                const contenedor = document.getElementById("productos");
                contenedor.appendChild(dropdown);

                const input = document.createElement("input");
                input.classList.add("form-control", "mx-4", "mt-2");
                input.setAttribute("placeholder", "Cantidad");
                input.setAttribute("name", "cantidad");
                input.setAttribute("value", 1);
                contenedor.appendChild(input);
            } catch (error) {
                console.error('Error:', error);
            }
        };

        const agregarProducto = document.querySelector('#agregar');
        agregarProducto.addEventListener("click", handleClick);

    });

</script>

<NavAdmin />

<div class="container mt-4 bg-white rounded shadow pt-5 pb-5 p-5 h-100 mb-5">

        <form on:submit|preventDefault={submitForm} id="form-product">
            
            <div class="mb-3">
                <label for="id_user" class="form-label">Selecciona el id del usuario</label>
                <select class="form-select" name="id_user" aria-label="Default select example">
                    {#each users as user}
                        <option value="{user.id}"> {user.id} </option>
                    {/each}
                </select>
            </div>

            <div class="mb-3">
                <label for="nombre" class="form-label">Latitud de la direccion</label>
                <input type="text" class="form-control" id="latitud" name="latitud">
            </div>
            
            <div class="mb-3 mt-4">
                <label for="direccion" class="form-label">Longitud de la direccion</label>
                <input type="text" class="form-control" id="longitud" name="longitud">
            </div>


            
            <div class="container mt-4 row g-3">
                <div class="col-auto">
                    <label readonly class="form-control-plaintext">Productos</label>
                </div>

                <div class="mx-4 col-auto">
                    <button type="button" id="agregar" class="btn mb-3 text-light" style="background-color:#6E6194;">Agregar producto</button>
                </div>
            </div>

            <div class="container input-group mb-3" id="productos"></div>

            <div class="mb-3 mt-5 justiy-content-center">
                <button type="submit" class="btn center w-100 btn-lg btn-block shadow-lg text-light" style=" background-color: #8973D9">Realizar pedido</button>
            </div>
        </form>
    </div>