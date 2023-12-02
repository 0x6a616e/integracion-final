import Login from './Login/Login.svelte';
import NuevoPedido from './User/NuevoPedido.svelte';
import DetallesPedido from './User/DetallesPedido.svelte';
import Pedidos from './User/Pedidos.svelte';
import PedidosAdmin from './Admin/PedidosAdmin.svelte';
import Sucursales from './Admin/Sucursales.svelte';
import Camiones from './Admin/Camiones.svelte';
import NuevoPedidoAdmin from './Admin/CRUD/NuevoPedidoAdmin.svelte';
import DetallesPedidoAdmin from './Admin/CRUD/DetallesPedidoAdmin.svelte'
import DetallesCamion from './Admin/CRUD/DetallesCamion.svelte';
import DetallesSucursal from './Admin/CRUD/DetallesSucursal.svelte';
import EditarCamion from './Admin/CRUD/EditarCamion.svelte';
import EditarSucursal from './Admin/CRUD/EditarSucursal.svelte';
import AsignarCamion from './Admin/CRUD/AsignarCamion.svelte';
import Estadisticas from './Admin/Estadisticas.svelte';

const routes = {
    '/':Login,
    '/nuevopedido':NuevoPedido,
    '/pedidos': Pedidos,
    '/detalles/pedido/:id': DetallesPedido,
    '/pedidos/admin': PedidosAdmin,
    '/sucursales': Sucursales,
    '/camiones':Camiones,
    '/nuevopedido/admin':NuevoPedidoAdmin,
    '/detalles/pedido/admin/:id': DetallesPedidoAdmin,
    '/detalles/camion/admin/:id': DetallesCamion,
    '/detalles/sucursal/admin/:id': DetallesSucursal,
    '/editar/camion/admin/:id': EditarCamion,
    '/editar/sucursal/admin/:id': EditarSucursal,
    '/asignar/camion/admin/:id':AsignarCamion,
    '/estadisticas': Estadisticas,
};

export default routes;