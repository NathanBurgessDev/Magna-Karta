//
//  Leather.swift
//  MagnaKartaApp
//
//  Created by James on 27/01/2024.
//

import SwiftUI

extension ShapeStyle where Self == AnyShapeStyle {
    static func leather(lightColor: Color, time: TimeInterval) -> Self {
        return AnyShapeStyle(ShaderLibrary.default.leather(
            .boundingRect,
            .color(lightColor),
            .float(time)
        ))
    }
}
