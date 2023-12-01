<script>

	import {link} from 'svelte-spa-router';

</script>

<div class="container bg-white rounded shadow pt-3 w-100"  style="height: 5rem;">
    <nav class="navbar navbar-expand-lg ">
        <div class="container-fluid">
          <span class="navbar-brand mb-0 h1"> Joyería Fina </span>
			<div class="collapse navbar-collapse" id="navbarSupportedContent">
				<ul class="navbar-nav me-auto mb-2 mb-lg-0" >
					
					<li class="nav-item">

					<a class="nav-link active" aria-current="page" href="/nuevopedido" use:link >Ordenar</a>

					</li>

					<li class="nav-item">

					<a class="nav-link active" aria-current="page" href="/pedidos" use:link>Pedidos</a>

					</li>

				</ul>
				<button class="btn btn-outline-danger" id="btn-logout">Log out</button>
			</div>
        </div>
    </nav>
</div>