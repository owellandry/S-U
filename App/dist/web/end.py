import json
from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para la aplicación

# Función para generar un ID único
def generar_id(registros_existentes):
    if not registros_existentes:
        return 1
    else:
        # Obtener el ID máximo actual y sumarle 1
        max_id = max(registro['id'] for registro in registros_existentes)
        return max_id + 1

# Ruta para obtener todos los registros o crear uno nuevo
@app.route('/api/tiempo', methods=['GET', 'POST'])
def tiempo_endpoint():
    if request.method == 'GET':
        try:
            # Cargar datos existentes desde data.json
            registros_existentes = []
            try:
                with open('data.json', 'r') as json_file:
                    registros_existentes = json.load(json_file)
            except FileNotFoundError:
                pass

            return jsonify(registros_existentes), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 500
    elif request.method == 'POST':
        try:
            data = request.get_json()
            tiempo = data.get('tiempo', 0)

            # Obtener la hora actual
            hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Crear un diccionario con el ID, la hora y el tiempo
            registro = {
                'id': generar_id(registros_existentes),
                'hora_solicitud': hora_actual,
                'tiempo': tiempo
            }

            # Cargar datos existentes desde data.json
            registros_existentes = []
            try:
                with open('data.json', 'r') as json_file:
                    registros_existentes = json.load(json_file)
            except FileNotFoundError:
                pass

            # Agregar el nuevo registro a la lista de registros
            registros_existentes.append(registro)

            # Guardar la lista actualizada en data.json
            with open('data.json', 'w') as json_file:
                json.dump(registros_existentes, json_file, indent=4)

            return jsonify({'message': 'Datos guardados correctamente'}), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 500

# Ruta para obtener un registro específico por su ID
@app.route('/api/tiempo/<int:id>', methods=['GET'])
def obtener_registro_por_id(id):
    try:
        # Cargar datos existentes desde data.json
        registros_existentes = []
        try:
            with open('data.json', 'r') as json_file:
                registros_existentes = json.load(json_file)
        except FileNotFoundError:
            pass

        # Buscar el registro con el ID especificado
        registro = next((r for r in registros_existentes if r['id'] == id), None)

        if registro is not None:
            return jsonify(registro), 200
        else:
            return jsonify({'error': 'Registro no encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
# Ruta para eliminar un registro específico por su ID
@app.route('/api/tiempo/<int:id>', methods=['DELETE'])
def eliminar_registro_por_id(id):
    try:
        # Cargar datos existentes desde data.json
        registros_existentes = []
        try:
            with open('data.json', 'r') as json_file:
                registros_existentes = json.load(json_file)
        except FileNotFoundError:
            pass

        # Buscar el registro con el ID especificado
        registro = next((r for r in registros_existentes if r['id'] == id), None)

        if registro is not None:
            # Eliminar el registro de la lista
            registros_existentes.remove(registro)

            # Guardar la lista actualizada en data.json
            with open('data.json', 'w') as json_file:
                json.dump(registros_existentes, json_file, indent=4)

            return jsonify({'message': 'Registro eliminado correctamente'}), 200
        else:
            return jsonify({'error': 'Registro no encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/api/tiempo', methods=['POST'])
def obtener_tiempo_endpoint():
    try:
        # Cargar datos existentes desde data.json
        registros_existentes = []
        try:
            with open('data.json', 'r') as json_file:
                registros_existentes = json.load(json_file)
        except FileNotFoundError:
            pass

        data = request.get_json()
        tiempo = data.get('tiempo', 0)

        # Obtener la hora actual
        hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Crear un diccionario con el ID, la hora y el tiempo
        registro = {
            'id': generar_id(registros_existentes),
            'hora_solicitud': hora_actual,
            'tiempo': tiempo
        }

        # Agregar el nuevo registro a la lista de registros
        registros_existentes.append(registro)

        # Guardar la lista actualizada en data.json
        with open('data.json', 'w') as json_file:
            json.dump(registros_existentes, json_file, indent=4)

        return jsonify({'message': 'Datos guardados correctamente'}), 200

    except Exception as e:
        print(e)  # Imprime el error en la consola para diagnóstico
        return jsonify({'error': str(e)}), 500



# Ruta para actualizar un registro específico por su ID
@app.route('/api/tiempo/<int:id>', methods=['PUT'])
def actualizar_registro_por_id(id):
    try:
        data = request.get_json()
        nuevo_tiempo = data.get('tiempo')

        # Cargar datos existentes desde data.json
        registros_existentes = []
        try:
            with open('data.json', 'r') as json_file:
                registros_existentes = json.load(json_file)
        except FileNotFoundError:
            pass

        # Buscar el registro con el ID especificado
        registro = next((r for r in registros_existentes if r['id'] == id), None)

        if registro is not None:
            # Actualizar el campo "tiempo" del registro
            registro['tiempo'] = nuevo_tiempo

            # Guardar la lista actualizada en data.json
            with open('data.json', 'w') as json_file:
                json.dump(registros_existentes, json_file, indent=4)

            return jsonify({'message': 'Registro actualizado correctamente'}), 200
        else:
            return jsonify({'error': 'Registro no encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
