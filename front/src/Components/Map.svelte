<script>
    import { onMount } from "svelte";
    
    export let x = 0;
    export let y = 0;
    onMount(() =>{
        var map = L.map('map').setView([x, y], 5); 
        L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        }).addTo(map);
        var marker = L.marker([x, y]).addTo(map);
    });
</script>

    <div id="map"></div>

<style>
    #map { 
        height: 30rem; 
        width: 30rem;
    }
</style>