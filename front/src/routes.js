import Login from './Login/Login.svelte';
import NuevoPedido from './User/NuevoPedido.svelte';
import DetallesPedido from './User/DetallesPedido.svelte';
import Pedidos from './User/Pedidos.svelte';
import PedidosAdmin from './Admin/PedidosAdmin.svelte';
import Sucursales from './Admin/Sucursales.svelte';
import Camiones from './Admin/Camiones.svelte';
import NuevoPedidoAdmin from './Admin/CRUD/NuevoPedidoAdmin.svelte';
import DetallesPedidoAdmin from './Admin/CRUD/DetallesPedidoAdmin.svelte'

const routes = {
    '/':Login,
    '/nuevopedido':NuevoPedido,
    '/pedidos': Pedidos,
    '/detalles/pedido/:id': DetallesPedido,
    '/pedidos/admin': PedidosAdmin,
    '/sucursales': Sucursales,
    '/camiones':Camiones,
    '/nuevopedido/admin':NuevoPedidoAdmin,
    '/detalles/pedido/admin/:id': DetallesPedidoAdmin
};

export default routes;