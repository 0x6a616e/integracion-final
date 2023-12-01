<script>
    import { onMount } from 'svelte';
	import { isAuthenticated } from '../js/auth';
    import NavUser from "../Components/NavUser.svelte";
    import Detalles from "../Components/Detalles.svelte";

</script>

<NavUser />

<Detalles x = 0 y = 0 items = {[]}/>


