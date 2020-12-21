<template>
  <div id="contendio">

    <h2 v-if="variableBooleana">Lista de los usuarios</h2>
    <table>
      <tr>
        <th>Cédula del usuario</th>
        <th>Nombre del usuario</th>
        <th>Apellido del usuario</th>
        <th>Teléfono del usuario</th>
        <th>E-mail del usuario</th>

      </tr>

      <tr v-for="cliente in lista_clientes">
        <td>{{ usuario.cedula }}</td>
        <td>{{ usuario.nombre }}</td>
        <td>{{ usuario.apellido }}</td>
        <td>{{ usuario.telefono }}</td>
        <td>{{ usuario.email }}</td>
  
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
      .get("http://127.0.0.1:8000/usuarios/listado/")
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
  font-weight: bold;
  color: rgb(255, 255, 255);
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