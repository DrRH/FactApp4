<template>
  <div id="contendio">

    <h2 v-if="variableBooleana">Lista de Usuarios del sistema</h2>
    <table>
      <tr>
        <th>Cédula del Usuario</th>
        <th>Nombre del Usuario</th>
        <th>Apellido del Usuario</th>
        <th>Rol del Usuario</th>
        <th>Teléfono del Usuario</th>
        <th>E-mail del Usuario</th>
        <th>Dirección del Usuario</th>
      </tr>

      <tr v-for="usuario in lista_usuarios">
        <td>{{ usuario.cedula }}</td>
        <td>{{ usuario.nombre }}</td>
        <td>{{ usuario.apellido }}</td>
        <td>{{ usuario.rol }}</td>
        <td>{{ usuario.telefono }}</td>
        <td>{{ usuario.email }}</td>
        <td>{{ usuario.direccion }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "verUsuarios",
  data: function() {
    return {
      variableBooleana: true,
      lista_usuarios: []
    };
  },
  beforeCreate: function() {
    axios
      .get("https://factapp4-v4.herokuapp.com/usuarios/listado")
      .then(response => {
        this.lista_usuarios = response.data;
      })
      .catch(error => {
        console.log(error);
        alert("Error del servidor");
      });
  }
};
</script>

<style scoped>

table,
th,
td {
  border: 1px solid rgb(96, 109, 187);
}

tr:first-child{
  background-color: #f0f0f0;
  font-weight: bold;
  color: #000;
}

table {
  position: relative;
  left: 50px;
  margin: auto;
  width: 100%;
  min-width: 375px;
  display: block;
  overflow-x: auto;
}

  .header h2{
    width: 50%;
    text-align:right;
    position: relative;

    }
@media screen and (min-width: 375px) {
  table {
    width: 100%;
    max-width: 800px;
  }
}
</style>