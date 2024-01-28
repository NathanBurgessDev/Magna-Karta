//
//  MockMoveRepository.swift
//  MagnaKartaApp
//
//  Created by James on 27/01/2024.
//

import Foundation

class MockMoveRepository: MoveRepository {
    override func move(x: Double, y: Double, completionHandler: @escaping ((Error)?) -> Void) {}
}
