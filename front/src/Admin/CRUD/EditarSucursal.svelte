<script>

    import Editar from "../../Components/Editar.svelte";
    import NavAdmin from "../../Components/NavAdmin.svelte";    
    export let params = {};
</script>

<NavAdmin />

<Editar label = "Sucursal" table = "branch" id = "{ params.id }"/>