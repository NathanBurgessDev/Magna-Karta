//
//  MoveRepository.swift
//  MagnaKartaApp
//
//  Created by James on 27/01/2024.
//

import Foundation

@Observable
class MoveRepository {
    private var ws: URLSessionWebSocketTask
    
    init() {
        let session = URLSession.shared
        ws = session.webSocketTask(with: URL(string: "ws://localhost:8765")!)
        ws.resume()
    }
    
    func move(x: Double, y: Double, completionHandler: @escaping ((Error)?) -> Void) {
        ws.send(.string("\(x),\(y)"), completionHandler: completionHandler)
    }
}
