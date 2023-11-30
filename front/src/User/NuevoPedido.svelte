<script>
    import NavUser from "../Components/NavUser.svelte";
    import { onMount } from 'svelte';
    import axios from 'axios';

    onMount(() => {

        const handleClick = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:5000/anillos');
                const data = response.data;

                const dropdown = document.createElement("select");
                dropdown.classList.add("form-select", "w-50", "mt-2");
                dropdown.setAttribute('name', 'modelo');

                data.forEach(objeto => {
                    const opcion = document.createElement("option");
                    opcion.text = objeto[0] + " | " + objeto[1];
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

<NavUser />

<div class="container mt-4 bg-white rounded shadow pt-5 pb-5 p-5 h-100 mb-5">
    <form action="/register-order" method="POST">
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