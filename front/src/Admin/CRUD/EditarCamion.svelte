<script>

    import Editar from "../../Components/Editar.svelte";
    import NavAdmin from "../../Components/NavAdmin.svelte";    
    export let params = {};
</script>

<NavAdmin />

<Editar label = "Camion" table = "truck" id = "{ params.id}"/>
