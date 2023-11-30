<script>
    import { onMount } from "svelte";
    onMount(() =>{
        var map = L.map('map').setView([51.5, -0.09], 13); 
        L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        }).addTo(map);
        var marker = L.marker([51.5, -0.09]).addTo(map);
    });
</script>

    <div id="map"></div>

<style>
    #map { 
        height: 30rem; 
        width: 30rem;
    }
</style>