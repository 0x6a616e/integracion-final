import Login from './Login/Login.svelte';
import NuevoPedido from './User/NuevoPedido.svelte';
import DetallesPedido from './User/DetallesPedido.svelte';
import Pedidos from './User/Pedidos.svelte';

const routes = {
    '/':Login,
    '/nuevopedido':NuevoPedido,
    '/pedidos': Pedidos,
    '/detallespedido/:id': DetallesPedido
};

export default routes;